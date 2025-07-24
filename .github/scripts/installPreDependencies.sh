#!/bin/bash
# This script installs pre dependencies prior to any package deployment for every scratch org in the pool
# (referenced in preDeploymentScriptPath attribute in project-[validate/dev]-pool-def.json)
sf org disable tracking --target-org # Disable source tracking to improve deployment performance