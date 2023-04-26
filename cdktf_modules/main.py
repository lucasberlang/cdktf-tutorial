#!/usr/bin/env python
from constructs import Construct
from cdktf import App, TerraformStack, TerraformOutput
from imports.google.provider import GoogleProvider
from imports.google_beta.provider import GoogleBetaProvider
from imports.gcp_pubsub import GcpPubsub
from imports.gcp_cloud_storage import GcpCloudStorage
import random
import string

class MyStack(TerraformStack):
    def __init__(self, scope: Construct, ns: str):
        super().__init__(scope, ns)



        GoogleProvider(self, "google", region="europe-west4")
        GoogleBetaProvider(self, "google-beta", region="europe-west4")
        length = 5
        suffix = ''.join((random.choice(string.ascii_lowercase) for x in range(length)))
        tags = {"provider" : "go",
                "region" : "euw4",
                "enterprise" : "bt",
                "account" : "poc",
                "system" : "ts",
                "environment" : "poc",
                "cmdb_name" : "",
                "security_exposure_level" : "mz",
                "status" : "",
                "on_service" : "yes"}

        topic = GcpPubsub(self,"topic",
          name = "cdktf-topic",
          project_id = "xxxxxxx",
          offset = 1,
          tags = tags)
          
        bucket = GcpCloudStorage(self,"bucket",
          name = "cdktf-test-1234-bt-" + suffix,
          project_id = "xxxxxxx",
          offset = 1,
          location = "europe-west4",
          lifecycle_rule = {},
          force_destroy = True,
          tags = tags)
        
        TerraformOutput(self,"topic_id",value=topic.id_output)
        TerraformOutput(self,"bucket_self_link",value=bucket.bucket_output)

app = App()
MyStack(app, "cdktf_modules")

app.synth()
