# Backend Challenges boilerplate - package.json

Use the ^ (Caret-Character) to Always Use the the Latest Minor Version of a Dependency

To allow an npm dependency to update to the latest MINOR version, you can prefix the dependency's version with the caret (^) character.

In the last exercise the current version should be 
    "moment": "~2.10.2", Using the tilde it allows us to update to the latest 2.10.x version.
    
    But if we were to use the caret (^) npm would be allowed to update to any 2.x.x verion


This is an example of how to allow minor updates to any version
    "moment": "^2.x.x",


