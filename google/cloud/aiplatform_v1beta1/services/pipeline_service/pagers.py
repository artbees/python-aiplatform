# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
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
#

from typing import Any, Callable, Iterable

from google.cloud.aiplatform_v1beta1.types import pipeline_service
from google.cloud.aiplatform_v1beta1.types import training_pipeline


class ListTrainingPipelinesPager:
    """A pager for iterating through ``list_training_pipelines`` requests.

    This class thinly wraps an initial
    :class:`~.pipeline_service.ListTrainingPipelinesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``training_pipelines`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListTrainingPipelines`` requests and continue to iterate
    through the ``training_pipelines`` field on the
    corresponding responses.

    All the usual :class:`~.pipeline_service.ListTrainingPipelinesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            [pipeline_service.ListTrainingPipelinesRequest],
            pipeline_service.ListTrainingPipelinesResponse,
        ],
        request: pipeline_service.ListTrainingPipelinesRequest,
        response: pipeline_service.ListTrainingPipelinesResponse,
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (:class:`~.pipeline_service.ListTrainingPipelinesRequest`):
                The initial request object.
            response (:class:`~.pipeline_service.ListTrainingPipelinesResponse`):
                The initial response object.
        """
        self._method = method
        self._request = pipeline_service.ListTrainingPipelinesRequest(request)
        self._response = response

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterable[pipeline_service.ListTrainingPipelinesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request)
            yield self._response

    def __iter__(self) -> Iterable[training_pipeline.TrainingPipeline]:
        for page in self.pages:
            yield from page.training_pipelines

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
