## Env Specific Alias Post vs. Env Specific packages
### Env Specific package
If the env specific metadata is not referenced by any other metadata

### Env Specific Alias Post
If the env specific metadata is referenced by other metadata. Then the metadata needs to also reside in a lower level package which is installed first. Then, when env-specific-alias-post is deployed, the values are overridden.
****NB!** Always keep the Production specific value in the lower level package!** Thus, there is no need for a prod directory here