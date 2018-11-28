# code snippets for the quickstart-create-workspace-with-python article
# <import>
import azureml.core
print(azureml.core.VERSION)
# </import>

# this is NOT a snippet.  If this code changes, go fix it in the article!
from azureml.core import Workspace
ws = Workspace.create(name='myworkspace',
                      subscription_id='65a1016d-0f67-45d2-b838-b8f373d6d52e',
                      resource_group='myresourcegroup',
                      create_resource_group=True,
                      location='eastus2' # or other supported Azure region
                     )

# <getDetails>
ws.get_details()
# </getDetails>

# <writeConfig>
# Create the configuration file.
ws.write_config()

# Use this code to load the workspace from 
# other scripts and notebooks in this directory.
# ws = Workspace.from_config()
# </writeConfig>

# <useWs>
from azureml.core import Experiment

# create a new experiment
exp = Experiment(workspace=ws, name='myexp')

# start a run
run = exp.start_logging()

# log a number
run.log('my magic number', 42)

# log a list (Fibonacci numbers)
run.log_list('my list', [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]) 

# finish the run
run.complete()
# </useWs>

# <viewLog>
print(run.get_portal_url())
# </viewLog>


# <delete>
# only delete the workspace.
ws.delete()

# CAUTION: delete the workspace AND its associated assets including storage account, ACR, KeyVault and AppInsights.
ws.delete(delete_dependent_resources=True)
# </delete>
