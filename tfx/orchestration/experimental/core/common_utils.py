# Copyright 2021 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Utils shared across modules."""

from typing import Optional

from tfx.proto.orchestration import pipeline_pb2

from google.protobuf import any_pb2


def get_executor_spec(pipeline: pipeline_pb2.Pipeline,
                      node_id: str) -> Optional[any_pb2.Any]:
  """Returns executor spec for given node_id if it exists in pipeline IR.

  Args:
    pipeline: Pipeline IR.
    node_id: Id of the node for which to get executor spec.

  Returns:
    An `any_pb2.Any` proto representing the executor spec or `None` if no
    executor spec can be found.
  """
  # TODO(b/170383494): Decide which DeploymentConfig to use.
  if not pipeline.deployment_config.Is(
      pipeline_pb2.IntermediateDeploymentConfig.DESCRIPTOR):
    return None
  depl_config = pipeline_pb2.IntermediateDeploymentConfig()
  pipeline.deployment_config.Unpack(depl_config)
  return depl_config.executor_specs.get(node_id)
