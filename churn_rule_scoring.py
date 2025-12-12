import snowflake.snowpark as snowpark

def main(session: snowpark.Session):

    # Read test customers from feature store
    test_df = session.table("TEST_CUSTOMERS")

    # Simple rule-based "model":
    # Predict churn (1) if TENURE < 6 OR SUPPORT_CALLS > 3, else 0
    scored_df = (
        test_df
        .with_column(
            "PREDICTION",
            ( (test_df["TENURE"] < 6) | (test_df["SUPPORT_CALLS"] > 3) ).cast("int")
        )
    )

    # Save predictions back to Snowflake
    scored_df.select("CUSTOMER_ID", "PREDICTION") \
             .write.save_as_table(
                 "CHURN_PREDICTIONS",
                 mode="overwrite"
             )

    return "Rule-based churn scoring completed."
