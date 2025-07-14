from prometheus_client import start_http_server, Summary, Counter


QUERY_TIME = Summary("query_duration_seconds", "Time spent answering a query")
QUERY_COUNT = Counter("user_query_count", "Total number of user queries")


def start_metrics_server(port=8000):
    start_http_server(port)


