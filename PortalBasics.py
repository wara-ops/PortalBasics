# ---
# jupyter:
#   jupytext:
#     cell_markers: '"""'
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
"""
# Using WARA-Ops data and resources

## Getting started

[WARA-Ops][1] is a portal consisting of two parts, *data sets* and *compute services*. The [data catalogue][2] holds the data sets. In this tutorial you will be using the data set "ERDClogs-parsed", which is *public*. Data on the portal is either public or *private*, meaning that access is restricted to users with the correct credentials. Regardless of classification, you need a token to access data on the portal.

A user's credentials are encoded in *token*, a long text string that looks like a random sequence of characters. In this tutorial you'll be guided through the steps of obtaining a token and loading data using the *data client* and your token.

The first step is to go to the [WARA-Ops][1] site on log in. Once logged in, you'll find yourself in the `Dataset catalog` section. If you click the `OVERVIEW` icon you can get a detail view of any of the available datasets by using the pop-up menu just below the icons. If you choose `5Gdata` you can see that it has *restricted access*, but the `ERDClogs-parsed` is classified as *open access*.

## Obtaining a token

Moving on by clicking the `JUPYTERHUB` icon you're on your way to the compute services part of the portal, but first you must generate a token by clicking the `GENERATE TOKEN` button at the bottom of the page. Click the `CREATE` button and then click `COPY` (or copy the text manually). Paste the text somewhere as you'll be needing it later. You'll only have to generate a new token after it has expired. Click outside the dialog to continue.

Next, click the `TO JUPYTERHUB` button to continue.

You'll (maybe) be asked to log in to the hub, ond once logged in click the `Start My Server` button. You should choose the `CPU server` at this point, the click `Start`. After a while you'll be in the Jupyter environment. If Jupyter is new to you, take a minute to check out the [documentation][3].

[1]: https://portal.wara-ops.org/home
[2]: https://portal.wara-ops.org/tabselect/DatasetCatalog
[3]: https://docs.jupyter.org/en/latest/
"""

# %% [markdown]
"""
## Acceesing data using the data client and your token

The first thing to do, is to import data portal client used to access the portal data:
"""
# %%
from dataportal import DataportalClient
# %%  [markdown]
"""
Next, we'll interact with the data portal, using the `DataportalClient` API. To do so you need your personal token from the portal.

Paste the token into the cell below, it should end up looking something like:

    # paste your token from the portal inside the quotes
    token = 'iOiJIUzI1NiIsInR5cCI6IkpXVCJ9.i4iLCJjbj13YXJhb3BzLXVzZXIsY249Z3JvdXBzLGNuPWF4iLCJjbj13YXJhb3BzLXVzZXIsY249Z3JvdXBzLGNuPWF'
    dataset = 'ERDClogs-parsed'
    client = DataportalClient(token)

Use `help(DataportalClient)` in a python cell to see some documentation.
"""
# %%
# paste your token from the portal inside the quotes
token = ''
dataset = 'ERDClogs-parsed'
client = DataportalClient(token)
# %% [markdown]
"""
After executing the above cell, it should print `Connection OK`, which means that the client is authenticated with the system.

However, before we can do anything we need to associate the client with a particular dataset:
"""
# %%
client.fromDataset(dataset)
# %% [markdown]
"""
Using the instantiated and configured client, we can examine the files in the dataset:
"""
# %%
file_iterator = client.listFiles()

# %% [markdown]
"""
Despite its name, `listFiles()` won't return a list of files, but an iteratable object so to use it we have to iterate over it (or force it to a list using `file_list = list(file_iterator)`)
"""
# %%
for file_info in file_iterator:
    print(file_info['FileID'])
# %% [markdown]
"""
We could pick any of the files, but we'll choose the file with FileID 36666:
"""
# %%
df = client.getData(fileID=36666) # load file content into a dataframe

# %% [markdown]
"""
Using `df.info()` provides some hints to the dataframe contents…
"""
# %%
df.info()

# %% [markdown]
"""
… as does `df.head()`.
"""
# %%
df.head()
# %%  [markdown] 
"""
That's it! You should now be ready to continue with the next tutorial. Remember that your token will be valid for all your sessions until it expires.
"""

