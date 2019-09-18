# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest

class UpdateStackRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ROS', '2019-09-10', 'UpdateStack','ROS')

	def get_StackPolicyDuringUpdateURL(self):
		return self.get_query_params().get('StackPolicyDuringUpdateURL')

	def set_StackPolicyDuringUpdateURL(self,StackPolicyDuringUpdateURL):
		self.add_query_param('StackPolicyDuringUpdateURL',StackPolicyDuringUpdateURL)

	def get_ClientToken(self):
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_query_param('ClientToken',ClientToken)

	def get_TemplateBody(self):
		return self.get_query_params().get('TemplateBody')

	def set_TemplateBody(self,TemplateBody):
		self.add_query_param('TemplateBody',TemplateBody)

	def get_StackId(self):
		return self.get_query_params().get('StackId')

	def set_StackId(self,StackId):
		self.add_query_param('StackId',StackId)

	def get_DisableRollback(self):
		return self.get_query_params().get('DisableRollback')

	def set_DisableRollback(self,DisableRollback):
		self.add_query_param('DisableRollback',DisableRollback)

	def get_EnableRecover(self):
		return self.get_query_params().get('EnableRecover')

	def set_EnableRecover(self,EnableRecover):
		self.add_query_param('EnableRecover',EnableRecover)

	def get_UpdateAllowPolicy(self):
		return self.get_query_params().get('UpdateAllowPolicy')

	def set_UpdateAllowPolicy(self,UpdateAllowPolicy):
		self.add_query_param('UpdateAllowPolicy',UpdateAllowPolicy)

	def get_TimeoutInMinutes(self):
		return self.get_query_params().get('TimeoutInMinutes')

	def set_TimeoutInMinutes(self,TimeoutInMinutes):
		self.add_query_param('TimeoutInMinutes',TimeoutInMinutes)

	def get_UsePreviousParameters(self):
		return self.get_query_params().get('UsePreviousParameters')

	def set_UsePreviousParameters(self,UsePreviousParameters):
		self.add_query_param('UsePreviousParameters',UsePreviousParameters)

	def get_TemplateURL(self):
		return self.get_query_params().get('TemplateURL')

	def set_TemplateURL(self,TemplateURL):
		self.add_query_param('TemplateURL',TemplateURL)

	def get_StackPolicyDuringUpdateBody(self):
		return self.get_query_params().get('StackPolicyDuringUpdateBody')

	def set_StackPolicyDuringUpdateBody(self,StackPolicyDuringUpdateBody):
		self.add_query_param('StackPolicyDuringUpdateBody',StackPolicyDuringUpdateBody)

	def get_StackPolicyURL(self):
		return self.get_query_params().get('StackPolicyURL')

	def set_StackPolicyURL(self,StackPolicyURL):
		self.add_query_param('StackPolicyURL',StackPolicyURL)

	def get_Parameterss(self):
		return self.get_query_params().get('Parameterss')

	def set_Parameterss(self,Parameterss):
		for i in range(len(Parameterss)):	
			if Parameterss[i].get('ParameterValue') is not None:
				self.add_query_param('Parameters.' + str(i + 1) + '.ParameterValue' , Parameterss[i].get('ParameterValue'))
			if Parameterss[i].get('ParameterKey') is not None:
				self.add_query_param('Parameters.' + str(i + 1) + '.ParameterKey' , Parameterss[i].get('ParameterKey'))


	def get_StackPolicyBody(self):
		return self.get_query_params().get('StackPolicyBody')

	def set_StackPolicyBody(self,StackPolicyBody):
		self.add_query_param('StackPolicyBody',StackPolicyBody)