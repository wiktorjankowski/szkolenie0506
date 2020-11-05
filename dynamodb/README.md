<img src="https://welastic.pl/wp-content/uploads/2020/05/cropped-welastic_logo-300x259.png" alt="Welastic logo" width="100" align="left">
<br><br>
<br><br>
<br><br>

# Introduction to DynamoDB using Python SDK

## LAB Overview

#### This lab will demonstrate:
  - Creating a role for EC2 instance
  - Creating a DynamoDB table
  - Uploading some data to DynamoDB table
  - Getting some data from DynamoDB table


## Task 1: Creating Cloud9 Environemnt
1.  In the AWS Management Console, on the **Services** menu, click **Cloud9**.
2.  Click **Create Environemnt**.
3.  Enter a **Name**: *student-x-cloud9*
4.  Choose **Create a new no-ingress EC2 instance for environment (access via Systems Manager)**
5.  Click **t3.small** as an **instance type**
6.  Leave everything else for default values
7.  Finish creation with click **Create Environemnt**.

## Task 2: Creating and attaching a EC2 role
Short description

1. In the AWS Management Console, on the **Services** menu, click **IAM**.
2. In the navigation pane on the left, click **Roles**.
3. Click **Create role**.
4. **Select type of trusted entity** choose: *AWS service*.
5. **Choose a use case** choose: *EC2*.
6. Click **Nest: Permissions**.
7. Find and select **AmazonDynamoDBFullAccess**.
8. Find and select **AWSCloud9SSMInstanceProfile**.
9. Click **Next: Tags**.
10. Click **Next: Review**.
11. Enter a name for your new role *student-X-EC2-Cloud9-DynamoDB-role*.
12. Click **Create role**.
13. In the AWS Management Console, on the **Services** menu, click **EC2**
14. Select your EC2 instance, click **Actions**,select **Instance Settings**, and then select **Attach/Replace IAM Role**.
15. Select the role you created in step 10 and click **Apply**.

## Task 3: Creating a DynamoDB table

1.  Open Cloud9 service and click **Open IDE** for your instance.
2.  If terminal exists please use it otherwise click in top menu **Window** and **New Terminal**
3.  Type: **sudo su**
4.  Run command ``pip install --upgrade --user boto3``.
5.  Create a folder by typing ``mkdir dynamodb``.
6.  Enter the directory ``cd dynamodb``.
7.  Create new file by typing ``nano create_dynamodb_table.py``.
8.  Download [create_dynamodb_table.py file](Files/create_dynamodb_table.py) and paste its content into editor.
9.  Edit table name.
10.  Press CTRL-O to save the file.
11.  Press CTRL-X to exit nano.
12.  Type ``python create_dynamodb_table.py`` to create the table.


## Task 4: Adding data

1.  In your Cloud9 terminal.
2.  Create new file by typing ``nano add_data.py``.
3.  Download [add_data.py file](Files/add_data.py) and paste its content into editor.
4.  Edit table name.
5.  Press CTRL-O to save the file.
6.  Press CTRL-X to exit nano.
7.  Type ``python add_data.py``.
8.  If there is no error reported, you should get a response.
9.  In the AWS Management Console, on the **Services** menu, click **DynamoDB**. Select your table and look into Items tabs.


## Task 5: Getting data

1.  Go back to your Cloud9 environment.
2.  Create new file by typing ``nano get_data.py``.
3.  Download [get_data.py file](Files/get_data.py) and paste its content into editor.
4.  Edit table name.
5.  Press CTRL-O to save the file.
6.  Press CTRL-X to exit nano.
7.  Type ``python get_data.py`` to retrieve some data.

If there is no error reported, you should get a response.

## Task 6: Adding index to a table (Global Secondary Index)

1.  In the AWS Management Console, on the **Services** menu, click **DynamoDB**.
2.  Find your table and clikc on its name.
3.  Select **Indexes**.
4.  Click **Create index**.
5.  Set *Address* as **Primary key**.
6.  Leave the rest unchanged and click **Create index**.

## Task 7: Querying data

1.  Go back to your Cloud9 environment.
2.  Create new file by typing ``nano query_data.py``.
3.  Download [query_data.py file](Files/query_data.py) and paste its content into editor.
4.  Edit table name.
5.  Press CTRL-O to save the file.
6.  Press CTRL-X to exit nano.
7.  Type ``python query_data.py`` to retrieve some data.
 
 You should get two items.

8. Edit file by typing ``nano query_data.py``.
9. Uncomment *FilterExpression* in line 13.

``FilterExpression='attribute_exists(Hobby)',``

10. Press CTRL-O to save the file.
11. Press CTRL-X to exit nano.
12. Type ``python query_data.py`` to retrieve some data.

Now you should get only 1 item.

## END LAB

Please delete your **DynamoDB** table.

<br><br>




<p align="right">&copy; 2020 Welastic Sp. z o.o.<p>
