# Sopra Steria Flxbl Template
A template for starting up new Flxbl projects

# 🧑‍💻 Setup

See [docs/devops](docs/devops) for instructions on how to setup this template in a new repo.

# 🤓 Develop

After all setup is done in the previous step, you're ready to develop!

You can now (typically):

-   Create feature branches and create PR's
-   This requires validation and code reviews, to ensure quality and safety before deploying to production
-   New changes merged to `main` are automatically deployed to `sit` and `preprod`
-   After a quick validation in preprod, you're good to go and can easily deploy to production 🎉

## First-time Install

Make sure you've performed the steps in [Local Setup](docs/devops/local-setup.md) before trying to create a Scratch Org.

## Clone Repo

1. Open the repo in your browser
1. Click `Code` → `Open with GitHub Desktop`
1. Save the repo somewhere on your computer
   - _**Avoid cloud-synced folders!**_
   - On Windows, the `Documents` folder is synced to OneDrive and will cause issues later!
1. In GitHub Desktop, click `Repository` → `Open in X`
   - Depending on your system you can have X = `Command Line`, `Git Bash` og `Terminal`
   - Once opened, type and run `npm install`
   - This will install all necessary software for you, including code formatting.

## Authenticate to Dev Hub
1. In the command line, run `sf auth web login -d -a [Company Name]`
   - This will open a browser window where you can log in to your Dev Hub org

## Make Changes

1. In GitHub Desktop, click `Repository` → `Open in X`
   - Depending on your system you can have X = `Command Line`, `Git Bash` og `Terminal`
1. Run `sfp pool:fetch -t dev -d -a "[alias]" -v [Company Name]`
   - Now, a fully functioning copy of production is fetched within seconds.
1. Run `sf project deploy start`
   - This will deploy changes that was merged on main branch after the Scratch Org was provisioned
1. Make your changes inside the Scratch Org
1. Run `sf project retrieve start` to add the changes from the Scratch Org to your local computer
1. Commit & Push the changes inside GitHub Desktop
1. Create a Pull Request
   - Get the changes validated successfully
   - If Slack Integration is working, a post is added for others to code review your changes. Otherwhise, get someone to approve it.
1. Merge the PR
1. Check the package creation status in the `Actions` tab
1. Once the package is done test your changes in the `preprod` environment
1. If everything looks good, you're ready to deploy to production!
   - Create a release branch, e.g. `release/my-feature` from the commit on `main` that contains the changes you want to release.
   - Update the release definition file (`.github/release-definitions` directory).
   - Navigate to the `[MANUAL] PROD Release` Action
   - Choose your release branch in the dropdown
   - Ensure the correct release definition is selected
   - Click `Run Workflow`
      - Wait a couple of seconds, and a new entry should appear in the list. You can open it to view the progress of the deployment.

# Template Updates

You can easily merge in new changes from the template

1. `git remote add template https://github.com/sopra-steria-salesforce/salesforce-dx-template`
1. `git fetch --all`
1. `git merge template/main --allow-unrelated-histories`

# 😴 Licensing

See [LICENSE](LICENSE), or summarised:

## Permissions

You're allowed to use this template:

-   For commercial use
-   For private use
-   To distribute it
-   To modify it

## Conditions

You must specify proper copyright notices. That means, somewhere in your code (e.g., the `LICENSE` file or the readme), you must link to this repository.

## Limitations

The author of this template refrains from any liability or warranty on the use of this template.