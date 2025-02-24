# Copyright (c) 2023 - 2025, AG2ai, Inc., AG2ai open-source projects maintainers and core contributors
#
# SPDX-License-Identifier: Apache-2.0
#
# Portions derived from  https://github.com/microsoft/autogen are under the MIT License.
# SPDX-License-Identifier: MIT
from typing import Any, Optional

from ...conversable_agent import ConversableAgent


class CriticAgent(ConversableAgent):
    """An agent for creating list of criteria for evaluating the utility of a given task."""

    DEFAULT_SYSTEM_MESSAGE = """You are a helpful assistant. You suggest criteria for evaluating different tasks. They should be distinguishable, quantifiable and not redundant.
    Convert the evaluation criteria into a list where each item is a criteria which consists of the following dictionary as follows
    {"name": name of the criterion, "description": criteria description , "accepted_values": possible accepted inputs for this key}
    Make sure "accepted_values" include the acceptable inputs for each key that are fine-grained and preferably multi-graded levels and "description" includes the criterion description.
    Output just the criteria string you have created, no code.
    """

    DEFAULT_DESCRIPTION = "An AI agent for creating list criteria for evaluating the utility of a given task."

    def __init__(
        self,
        name="critic",
        system_message: Optional[str] = DEFAULT_SYSTEM_MESSAGE,
        description: Optional[str] = DEFAULT_DESCRIPTION,
        **kwargs: Any,
    ):
        """Args:
        name (str): agent name.
        system_message (str): system message for the ChatCompletion inference.
            Please override this attribute if you want to reprogram the agent.
        description (str): The description of the agent.
        **kwargs (dict): Please refer to other kwargs in
            [ConversableAgent](/docs/api-reference/autogen/ConversableAgent#conversableagent).
        """
        super().__init__(
            name=name,
            system_message=system_message,
            description=description,
            **kwargs,
        )
