import mlflow

def select_best_run(metric_name="rmse"):
    client = mlflow.tracking.MlflowClient()
    experiment = client.get_experiment_by_name("Default")

    runs = client.search_runs(
        experiment_ids=[experiment.experiment_id],
        order_by=[f"metrics.{metric_name} ASC"]
    )

    best_run = runs[0]

    print("Best Run ID:", best_run.info.run_id)
    print("Best Metric Value:", best_run.data.metrics[metric_name])

    return best_run.info.run_id


if __name__ == "__main__":
    select_best_run()
