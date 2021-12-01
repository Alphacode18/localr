import os
import sys
from storage import storage
from input import generate_input
from function import handler

store = storage()
client = store.client
ROOT_DIR = os.path.abspath("../..")

client.make_bucket("504.dna-visualization-in")
client.make_bucket("504.dna-visualization-out")

def cleanup(bucket, object_name):
  client.remove_object(bucket, object_name)

for iteration in range(0, 1000):
  input_conf = generate_input(data_dir=os.path.join(ROOT_DIR, "benchmarks", "data", "504.dna-visualization"),
                              input_buckets=["504.dna-visualization-in"],
                              output_buckets=["504.dna-visualization-out"],
                              upload_func=store.upload)
  input_conf['object']['store'] = store
  handler(iteration, input_conf)
  cleanup("504.dna-visualization-in", input_conf['object']['key'])
  cleanup("504.dna-visualization-out", input_conf['object']['key'])