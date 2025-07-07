# Setup Repo

This documentation is for when you want to setup the Flxbl DevOps framework for your project 🎉

1. On the [salesforce-dx-template](https://github.com/sopra-steria-salesforce/flxbl-template) main page, click `Use this template` and give your repo a name
    - Do _**not**_ copy branches
1. From now on, all changes described are to be done on the new repo you just created
1. Go to `Settings` → `Collaborators and teams`
    - Add whoever needs access.
1. Add secrets
    - Secrets can be added globally (GitHub org settings), in a specific repo (repo settings) or using environments. Unsure? Repo settings is a safe bet.
    - In org or repo settings → `Secrets and Variables` → `Actions`
    - Add the needed secrets (see [Secrets](#secrets) below)
1. Initialise repo
    - **Make sure all secrets are added before this step!**
    - The last step! This step will automatically set labels, settings, rulesets, environments, create first GitHub release, Salesforce Unlocked Package and create preprod branch
    - On your new repo → `Actions` tab → `Show more workflows...` → `[X] Initialise/Update Repo` → `Run workflow`
    - Ensure the job runs successfully. You can retry or re-run the job safely if something failed.
1. Your repo should now be done! 🎉
    - Go to the main page of your new repo, and look for the header `Making Changes and Deployment` for further instructions.



# Secrets

<!-- prettier-ignore -->
| Name                                                                     | Description                                                                         | Required? |
|--------------------------------------------------------------------------|-------------------------------------------------------------------------------------|----------|
| `SF_PACKAGE_KEY`                                                         | Can be whatever you want.<br>But it's a password every developer needs to remember. | ✅        |
| `PROD_SFDX_AUTH_URL`<br>`PREPROD_SFDX_AUTH_URL`<br>`SIT_SFDX_AUTH_URL` | See [Create SF CLI Integration User](##Create SF CLI Integration User)                     | ✅        |

## Create SF CLI Integration User

You will need one dedicated user in every Salesforce instance to deploy on behalf of every developer. This is an integration user with enough access in production (or preprod) to deploy metadata through the Metadata API. It should not have any unecessary access not needed or even access to the GUI, to reduce the impact if the credentials to the user should be leaked. It won't even have a password, just a private key needed to be able to login into the user.

1. Open Production → Setup → Users → `New User`
    - **First Name**: `SF CLI`
    - **Last Name**: `INTEGRATION USER`
    - **Email**: your own
    - **Username**: `SF.CLI.INTEGRATION.USER@company.no`
    - **Profile**: `System Administrator`
    - Click `Save`
1. Create a new permission set named `sf_cli_integration_user`
    - With the following System Permissions:
        - `API Enabled`
        - `Api Only User`
        - `Create and Update Second-Generation Packages`
        - `Delete Second-Generation Packages`
        - `Modify Metadata Through Metadata API Functions`
    - With the following Object Settings: (PRODUCTION ONLY)
        - `Active Scratch Orgs`: `modify all`
        - `Scratch Org Infos`: `modify all`
1. Assign the permission set to the new integration user
1. Add Secret in GitHub
    - Authorize to PROD using sf auth web login -a [Company Name] -r https://login.salesforce.com
        - Using the credentials of the integration user you just created
    - Run sf org display -o [Company Name] --verbose
    - Copy the `SFDX Auth URL` and store it as the secret `PROD_SFDX_AUTH_URL`
    - **NB!** Remember to log out of the integration user after this step, using `sf auth logout -o [Company Name]`
1. Do everything again, but for `preprod` and `sit`
    - **NB!** Use -r https://test.salesforce.com