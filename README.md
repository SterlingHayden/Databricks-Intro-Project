# Databricks-Intro-Project
My notes as I figure out how to use Azure Databricks.
Azure Databricks documentation avaliable [here](https://learn.microsoft.com/en-us/azure/databricks/introduction/).  


Steps to creating Workspace:  
1. From Azure Databricks, create a Databricks workspace with the specific details required for your project.  
2. Once the workspace is successfully created, launch it. This step will take you to the Databricks environment.  
3. Now we need to create the appropriate cluster for our task. In the context of Databricks, a cluster is a group of virtual machines that work together to process and analyze data. The choice of cluster specifications depends on the nature of your tasks, such as data processing or machine learning.
4. In your workspace, create a notebook. Inside the notebook, you'll need to connect the cluster that you just created. Additionally, you can rename the notebook and change the program language to match your project requirements. 


Adding data to the workspace:  
1. Data can be added through varrious methods in Databricks. For my beginner use case and for the fun of it I'm going to call an api (you can install new libraries inside your cluster, linked [here](https://caiomsouza.medium.com/azure-databricks-installing-a-python-library-a511938ddfe)).  
2. 