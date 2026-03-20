import pandas as pd


def model(dbt, session):
    dbt.config(materialized="table")

    # source 테이블
    p_events = dbt.source("p_source", "p_events")
    p_transactions = dbt.source("p_source", "p_transactions")

    # pandas 변환
    events_df = p_events.to_pandas()
    trans_df = p_transactions.to_pandas()

    # -----------------------------
    # 1. first_touch 계산
    # -----------------------------
    events_df = events_df.sort_values(['CUSTOMER_ID', 'EVENT_TS'])

    first_touch = (
        events_df
        .groupby('CUSTOMER_ID')['TRAFFIC_SOURCE']
        .first()
        .str.upper()
        .reset_index()
    )

    # -----------------------------
    # 2. customer_revenue 계산
    # -----------------------------
    customer_revenue = (
        trans_df
        .groupby('CUSTOMER_ID')['GROSS_REVENUE']
        .sum()
        .reset_index()
        .rename(columns={'GROSS_REVENUE': 'TOTAL_REVENUE'})
    )

    # -----------------------------
    # 3. JOIN
    # -----------------------------
    merged = pd.merge(
        first_touch,
        customer_revenue,
        on='CUSTOMER_ID',
        how='inner'
    )

    # -----------------------------
    # 4. traffic_source 기준 집계
    # -----------------------------
    result = (
        merged
        .groupby('TRAFFIC_SOURCE')['TOTAL_REVENUE']
        .sum()
        .reset_index()
        .rename(columns={'TOTAL_REVENUE': 'REVENUE'})
    )

    return result