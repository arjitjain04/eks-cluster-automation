import pulumi


class EKSConfigHandler:
    def __init__(self):
        self.cluster_config = pulumi.Config("cluster")
        self.monitoring_config = pulumi.Config("monitoring")

    def handle_cluster_config(self):
        cluster_vars = {
            "cluster_name": self.cluster_config.require("name"),
            "cluster_version": self.cluster_config.require("version"),
            "cpu_instance_type": self.cluster_config.require(
                "cpu_instance_type"
            ),
            "desired_cpu_node_count": self.cluster_config.require_int(
                "desired_cpu_node_count"
            ),
            "min_cpu_node_count": self.cluster_config.require_int(
                "min_cpu_node_count"
            ),
            "max_cpu_node_count": self.cluster_config.require_int(
                "max_cpu_node_count"
            ),
            "cpu_node_disk_size": self.cluster_config.require_int(
                "cpu_node_disk_size"
            ),
            "gpu_operator_version": self.cluster_config.require(
                "gpu_operator_version"
            ),
            "gpu_instance_type": self.cluster_config.require(
                "gpu_instance_type"
            ),
            "desired_gpu_node_count": self.cluster_config.require_int(
                "desired_gpu_node_count"
            ),
            "min_gpu_node_count": self.cluster_config.require_int(
                "min_gpu_node_count"
            ),
            "max_gpu_node_count": self.cluster_config.require_int(
                "max_gpu_node_count"
            ),
            "gpu_node_disk_size": self.cluster_config.require_int(
                "gpu_node_disk_size"
            ),
        }
        return cluster_vars

    def handle_monitoring_config(self):
        monitoring_vars = {
            "namespace": self.monitoring_config.require("namespace"),
            "external_services_prometheus_host": self.monitoring_config.require(
                "external_services_prometheus_host"
            ),
            "external_services_prometheus_basicauth_username": self.monitoring_config.require(
                "external_services_prometheus_basicauth_username"
            ),
            "external_services_prometheus_basicauth_password": self.monitoring_config.require(
                "external_services_prometheus_basicauth_password"
            ),
            "external_services_loki_host": self.monitoring_config.require(
                "external_services_loki_host"
            ),
            "external_services_loki_basicauth_username": self.monitoring_config.require(
                "external_services_loki_basicauth_username"
            ),
            "external_services_loki_basicauth_password": self.monitoring_config.require(
                "external_services_loki_basicauth_password"
            ),
            "external_services_tempo_host": self.monitoring_config.require(
                "external_services_tempo_host"
            ),
            "external_services_tempo_basicauth_username": self.monitoring_config.require(
                "external_services_tempo_basicauth_username"
            ),
            "external_services_tempo_basicauth_password": self.monitoring_config.require(
                "external_services_tempo_basicauth_password"
            ),
            "external_services_shoreline_namespace": self.monitoring_config.require(
                "external_services_shoreline_namespace"
            ),
            "external_services_shoreline_customer_id": self.monitoring_config.require(
                "external_services_shoreline_customer_id"
            ),
            "external_services_shoreline_shoreline_customer_secret": self.monitoring_config.require(
                "external_services_shoreline_shoreline_customer_secret"
            ),
            "external_services_shoreline_shoreline_customer_endpoint": self.monitoring_config.require(
                "external_services_shoreline_shoreline_customer_endpoint"
            ),
            "external_services_shoreline_certificate": self.monitoring_config.require(
                "external_services_shoreline_certificate"
            ),
            "external_services_shoreline_resource_image": self.monitoring_config.require(
                "external_services_shoreline_resource_image"
            ),
            "external_services_shoreline_resource_tag": self.monitoring_config.require(
                "external_services_shoreline_resource_tag"
            ),
            "external_services_shoreline_resources_cpu_limits": self.monitoring_config.require(
                "external_services_shoreline_resources_cpu_limits"
            ),
            "external_services_shoreline_resources_memory_limits": self.monitoring_config.require(
                "external_services_shoreline_resources_memory_limits"
            ),
            "external_services_shoreline_resources_cpu_requests": self.monitoring_config.require(
                "external_services_shoreline_resources_cpu_requests"
            ),
            "external_services_shoreline_resources_memory_requests": self.monitoring_config.require(
                "external_services_shoreline_resources_memory_requests"
            ),
            "metrics_enabled": self.monitoring_config.require_bool(
                "metrics_enabled"
            ),
            "metrics_alloy_metricstuning_useintegrationallowlist": (
                self.monitoring_config.require_bool(
                    "metrics_alloy_metricstuning_useintegrationallowlist"
                )
            ),
            "metrics_cost_enabled": self.monitoring_config.require_bool(
                "metrics_cost_enabled"
            ),
            "metrics_node_exporter_enabled": self.monitoring_config.require_bool(
                "metrics_node_exporter_enabled"
            ),
            "logs_enabled": self.monitoring_config.require_bool(
                "logs_enabled"
            ),
            "logs_pod_logs_enabled": self.monitoring_config.require_bool(
                "logs_pod_logs_enabled"
            ),
            "logs_cluster_events_enabled": self.monitoring_config.require_bool(
                "logs_cluster_events_enabled"
            ),
            "traces_enabled": self.monitoring_config.require_bool(
                "traces_enabled"
            ),
            "receivers_grpc_enabled": self.monitoring_config.require_bool(
                "receivers_grpc_enabled"
            ),
            "receivers_http_enabled": self.monitoring_config.require_bool(
                "receivers_http_enabled"
            ),
            "receivers_zipkin_enabled": self.monitoring_config.require_bool(
                "receivers_zipkin_enabled"
            ),
            "receivers_grafanacloudmetrics_enabled": self.monitoring_config.require_bool(
                "receivers_grafanacloudmetrics_enabled"
            ),
            "opencost_enabled": self.monitoring_config.require_bool(
                "opencost_enabled"
            ),
            "kube_state_metrics_enabled": self.monitoring_config.require_bool(
                "kube_state_metrics_enabled"
            ),
            "prometheus_node_exporter_enabled": self.monitoring_config.require_bool(
                "prometheus_node_exporter_enabled"
            ),
            "prometheus_operator_crds_enabled": self.monitoring_config.require_bool(
                "prometheus_operator_crds_enabled"
            ),
            "extraConfig": self.monitoring_config.require("extraConfig"),
        }
        return monitoring_vars
