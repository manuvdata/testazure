#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "dbd267a0-1141-4087-8cf2-a77bd477d6bc")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "b5319493-ba5e-4ed1-bace-0252c23ef634")
