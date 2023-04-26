#!/usr/bin/env python
from constructs import Construct
from cdktf import App, TerraformStack, TerraformOutput
from imports.google.provider import GoogleProvider
from imports.google.storage_bucket import StorageBucket
from imports.google.pubsub_topic import PubsubTopic
import random
import string

class MyStack(TerraformStack):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        GoogleProvider(self, "google", region="europe-west4",project="xxxxxx")
        length = 5
        suffix = ''.join((random.choice(string.ascii_lowercase) for x in range(length)))
        bucket = StorageBucket(self, "gcs", name = "cdktf-test-1234-bt-"+ str(suffix), location = "EU", force_destroy = True)
        topic = PubsubTopic(self, "topic" ,name = "cdktf-topic", labels={"tool":"cdktf"})
        TerraformOutput(self,"bucket_self_link",value=bucket.self_link)
        TerraformOutput(self,"topic-id",value=topic.id)

app = App()
MyStack(app, "first_steps")

app.synth()
