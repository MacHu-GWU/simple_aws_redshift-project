# -*- coding: utf-8 -*-

from simple_aws_redshift.tests.settings import settings

stack_ctx = settings.stack_ctx

# --- 📦 cdk synth
# stack_ctx.cdk_synth(dir_cdk=__file__)

# --- 🔍 cdk diff
# stack_ctx.cdk_diff(dir_cdk=__file__)

# --- 🚀 cdk deploy
stack_ctx.cdk_deploy(dir_cdk=__file__, prompt=False)

# --- 💥 cdk destroy
# stack_ctx.cdk_destroy(dir_cdk=__file__, prompt=False)
