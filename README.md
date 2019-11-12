# Jesterworks
My general purpose root ntuple cutting and skimming code.

## Jesterworks.py
This is the main running script. It runs on a defined number of Jesterworks configuration files. 

## Config definitions
This module contains most of the definitions and classes necessary to create a final configuration.

### JesterworksConfigurations.py
This contains the definition of the top level configuration class. Everything All inputs to the final script will
need to be instances of this particular class, with proper user substituted values.

#### Options
- `--ConfigFiles` (Required) Takes any number of arguments. Should just be paths to the final configurations to be run
- `--CreateCutFlow` (Optional) Creates and adds a cutflow plot to the final output.
  This cutflow plot is created by performing each cut individually one at a time, and so is somewhat time consuming.
  This option should really be only used for debug purposes. The first bin of the cutflow represents the number of
  entries in the tree before any cuts, and each subsequent bin represents the number of entries in the tree after each
  cut in your cutting configuration, applied in the sequence you wrote them.

### UserConfigs
Contains user definitions of the top level configurations used to run the tool. Configurations aren't *required* to
go in here, but it does create a convenient spot for them.

#### How do I write a final configuration?

- Open up a python file. At the top import the configuration definition: `from ConfigDefinitions.JesterworksConfigurations import JesterworksConfiguration as Config `
- At the top, you should also import the branch collection (see branch additions), the cutting definitions (see cutting definitions), and any end action you would like to be performed.
- All configurations are just instances of the configuration class that can be imported to the main script later. 
  to start making a configuration, just create an instance of the config, e.g: `DataConfig = Config()`
- (optional) You can then set a path to search for any of the files by setting the config's `Path` variable.
  Full paths can be specified in the `Files` list variable, but this option can keep the list looking a little cleaner.
- Create a list of the files you would like merged together and cut, and set the config's `Files` variable to this list.
  e.g. `Files = ["Fil1.root","File2.root","File3.root"]
- Set the config variable `InputTreeName` to the name of the original tree in the files to be cut.
- Set the config variable `SampleName` to a convenient name for your sample. This has no instrisic behavior, but can
  be used to control other behavior you write later if you would like.
- Set the config variable(s) `OutputPath` and `OutputFile` to the path you would like your cut files placed in, and     the name of the file, respectively
- Set the config variable `OutputTreeName` to the name of the final tree you would like in the cut files.
- (optional) if you have defined a collection of branches you would like added to the final files, set the config 
  variable `BranchCollection` to this collection
- Set the config variable `CutConfig` to the defined cutting configuration for this sample.
- (optional) if you have end actions defined, you can set that to the `EndAction` variable in the configuration.

### Cutting Definitions
Contains defintions for cuts to be applied to the tree.

#### CutDef.py
This creates the simple class used to define a cutting configuration.

#### UserCutConfigs
Just a convenient space for storing all of your cutting configurations.

#### How do I write all my cuts into a configuration?
To write the configuration:
- Open a python file, at the top import the the the cutting defintion with: `from ConfigDefinitions.CuttingDefinitions.CutDef import UserCutConfig as CutConfig`
- Create an instance of the cutting configuration with: `MyCuts = CutConfig()`
- Because of a weird quirk of using these configruations, the `Cuts` config list needs to be reset at the top of 
  the configuration like so: `MyCuts.Cuts = []`
- Append all your cuts to the list with `MyCuts.Cuts.append(TheCut)`. Cuts will be processed by TTree's CopyTree()
  function and so must be readable as basic C based logic and math.
- Cuts should be kept as seperate by purpose as possible.

### Branch Additions
Contains definitions for branches to be added to the tree. Note, all branches are added to the tree *before* the tree 
is cut. This can be computationally expensive, but also makes these values available for cutting on in case all the 
values you would like to be cut are not natively stored to the tree.

#### BranchDef.py
This contains definitions both for the UserBranch class, which is used to define an individual branch to be added to 
the final cut product, and UserBranchCollection, which is used to contain a list of branches for the configuration to
add multiple branches at a time.

I find this useful to do things like add MT, or branches that contain flags for meeting trigger requirements to my
final product.

#### UserDefinedBranches
Just a convenient spot for putting any code and configurations used for writing your UserBranch

#### UserDefinedCollections
Just a convenient spot for putting any code and configurations used for writing your UserBranchCollections.

#### How do I write a new branch and get it added to my final product?
First we need to write the actual branch itself:
- Open up a python file. At the top of this file, import the branch definition: `import ConfigDefinitions.BranchAdditions.BranchDef as Branch`
- import anything else you may need (I will often need math packages for example).
- Write a function that performs the calculation of the branch's value. This function must take two arguments. 
  The first is the actual UserBranch object that is being added itself. The second is the tree with the current 
  entry loaded. I find it useful to label these variables `TheBranch` and `TheChain` myself, but this is not
  strictly necessary. By the end of this function, you must set `TheBranch.BranchValue[0]` to the value you 
  want stored in the branch, for this particular entry in the tree.
- Now we can write the actual branch itself. This should be easy, it should only need three lines
- First, create an instance of the a user branch: `MyBranch = Branch.UserBranch()`
- Then, set it's name. This will be the branch's name in the tree after the cutting is done, `MyBranch.Name = 'MyBranch'`
- Then, set the branch's `CalculateValue` function to the function you have made for computing the branch like so; `MyBranch.CalculateValue = MyFunction`. Note the lack of parentheses and arguments.
Now, we need to write a collection for it to be a part of. Collections allow multiple branches to get added at once, 
so if you need, you can go and write all the branches you need and make them a part of one collection. Writing the 
collection should be very simple, little more than just listing all the branches/variables you made explicitly in one
spot. To write one:
- Open up a python file. At the top of this file, import the branch definition: `import ConfigDefinitions.BranchAdditions.BranchDef as BranchDef`
- Import each of the UserBranches you just made
- Declare an instance of the collection, `MyCollection = BranchDef.UserBranchCollection()`
- Set the collections `UserBranches` variable to a list containing all the UserBranch objects you just made and imported: e.g.: `MyCollection.UserBranches = [MyBranch,MyOtherBranch,MyThirdBranch]`
Now this should be ready for use in your main configuration, and any other configurations you may need to write in the future.

### End Action Definitions
Contains defintions for actions that are performed at the end of all cutting

#### EndActionDef.py
Contains the definition for end actions

#### UserConfigs
Just a convenient spot to place all user defined end actions.

#### How do I write an end action?
- Open up a python file and import the end action definition: `import ConfigDefinitions.EndActionDefinitions.EndActionDef as EndActionDef`
- Define a function that takes four arguments, the end action itself, the cut tree, the final configuration, and the output file object. This function can do ... whatever with these objects.
- Write the end action itself. This is two lines, create an instance of UserEndAction, and then set it's `PerformEndAction` to the function you have just written.

## JesterworksUtils
Contains quick utility scripts for use throughout the Jesterworks package.

### Colors.py
Contains some definition for ANSI codes for output

### CutFlowCreator.py
A module with the code used to create cutflow plots to include with the final output

### RecursiveLoader.py
File containing the object I wrote to load python modules from directory paths.

## What do I have to do to get this running and make my final output?

Once you have all the configurations you need defined and collected into a final configuration, it is as simple as:
`python Jesterworks.py --ConfigFiles <Configurations to be run. Wildcards work here if necessary>`

## About the name
Weird story.

If you have any upgrades or any ideas for improvement, I would love to see this tool see use beyond just myself!
