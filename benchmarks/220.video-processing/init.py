import os
from storage import storage
from input import generate_input
from function import handler

store = storage()
client = store.client
ROOT_DIR = os.path.abspath("../..")

client.make_bucket("220.video-processing-in")
client.make_bucket("220.video-processing-out")

def cleanup(bucket, object_name):
  client.remove_object(bucket, object_name)

for iteration in range(0, 1000):
  input_conf = generate_input(data_dir=os.path.join(ROOT_DIR, "benchmarks", "data", "220.video-processing"),
                              input_buckets=["220.video-processing-in"],
                              output_buckets=["220.video-processing-out"],
                              upload_func=store.upload)
  input_conf['object']['store'] = store
  handler(iteration, input_conf)
  cleanup("220.video-processing-in", input_conf['object']['key'])
  cleanup("220.video-processing-out", f"processed-{input_conf['object']['key']}")