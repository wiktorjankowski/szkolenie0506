<img src="https://welastic.pl/wp-content/uploads/2020/05/cropped-welastic_logo-300x259.png" alt="Welastic logo" width="100" align="left">
<br><br>
<br><br>
<br><br>

# API Gateway - Introduction

## LAB Overview

#### In this lab we will create API using API Gateway service and will connect it to Lambda function. We'll use API Gateway both as proxy and not.

## Task 1: Creating a Lambda function

1. In the AWS Management Console, on the **Services** menu, click **Lambda**.
2. Click **Create function**.
3. Select **Autor from scratch**.
4. Enter a name for the function: *student-X-api*.
5. Select **Python 3.7** as **Runtime**.
6. Click **Create function**.
7. Download [lambda file](lambda.py) and paste its content as Lambda source code.
8. Scroll down and check the checmark left to the **Enable active tracing**
9. Click **Save**.

## Task 2: Creating API using API Gateway

1.  In the AWS Management Console, on the **Services** menu, click **API Gateway**.
2.  Click **Build** in the **REST API** box. 
4.  Choose **New API**.
5.  Enter a name for your API: *student-X-api*.
6.  Set **Endpoint Type** to **Regional**.
7.  Click **Create API**.

## Task 3: Adding resources and methods to API.

1.  Click **Actions**.
2.  Select **Create Resource**.
3.  Enter a name for **Resource Name**: *hello*.
4.  Click **Create resource**.
5.  Select **/hello** and click **Actions**.
6.  Select **Create Method**.
7.  Select **GET** from the dropdown.
8.  Click checkmark button.
9.  Select **Lambda function** as **Integration type**.
10. Turn **Use Lambda Proxy integration** on.
11. Set your function created in task 1 as **Lambda Function**.
12. Click **Save**.
13. Select your main resource.
14. Click **Actions**.
15. Select **Create Resource**.
16. Enter a name for **Resource Name**: *hello2*.
17. Click **Create resource**.
18. Select **/hello2** and click **Actions**.
19. Select **Create Method**.
20. Select **GET** from the dropdown.
21. Click checkmark button.
22. Select **Lambda function** as **Integration type**.
23. Leave **Use Lambda Proxy integration** unchecked.
24. Set your function created in task 1 as **Lambda Function**.
25. Click **Save**.

## Task 4: Deploying API

1.  Click **Actions**.
2.  Select **Deploy API**.
3.  Select **[New stage]** as **Deployment stage**.
4.  Enter a name for your stage.
5.  Click **Deploy**.
6.  At the bottom ofleft menu select **Settings**.
7.  In the **CloudWatch log role ARN** paste the ARN given by instructor. -> arn:aws:iam::536966783968:role/lab2-rola-apigateway
8.  Click **Save**.
9.  Select your stage and click **Logs/Tracing**.
10. Turn on:
  **Enable CloudWatch Logs** (and set **Log Level** to **INFO**)
* **Log full requests/responses data**
* **Enable Detailed CloudWatch Metrics**
* **Enable X-Ray Tracing**
11. Click **Save changes**

## Task 5: Invoking both endpoints

1.  Invoke endpoints related to both resources, *hello* and *hello2*. You can repeat that several times.
2.  Go back to your Lambda function configuration page.
3.  Click **Monitoring**.
4.  Click **View logs in CloudWatch**
5.  Click on the topmost LogStream and examine the difference between logged event objects.

## Task 6: Adding authorizer

1.  In the AWS Management Console, on the **Services** menu, click **Lambda**.
2.  Click **Create function**.
3.  Enter a name, e.g. "student-X-auth-lambda".
4.  Select **Python 3.6** as a runtime.
5.  Choose **Create a new role from AWS policy templates** as a **Role**.
6.  Enter a name for the role, e.g. "auth-lambda-role".
7.  Click **Create function**.
8.  Download [auth_lambda.py](auth_lambda.py) file and copy its content into editor field.
9. Scroll down to Section **Environment variables**
10. Click **Manage environment variables**
11. Click **Add environment variable**
12. Set a value for key *auth_token* environment variable. (Select your own)
13. Click **Save** to save env and **Deploy** to update Lambda itself.
14. In the AWS Management Console, on the **Services** menu, click **API Gateway**.
15. Find your API and click on its name.
16. Click **Authorizers** and **Create New Authorizer**.
17. Enter a name for your authorizer, e.g. "auth-lambda-authorizer".
18. Set **Lambda** as the type.
19. Select your authorization Lambda which you prepared in the previous step.
20. Select **Token** as a **Lambda Event Payload**.
21. Enter a **Token Source**. Set it to "Authorization". This is the request header which will be sent to your Lambda function.
22. Set **TTL** to 30 seconds.
23. Click **Create**.
24. Click **Grant & Create** if needed.
25. Click **Test**.
26. Type your correct auth token value (the value you used in environment variables for your Lambda function).
27. Click **Test** once again.
28. Enter different value for test token and test it again. You should get a policy with explicit *Deny*.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Deny",
      "Action": "execute-api:Invoke",
      "Resource": "arn:aws:execute-api:eu-west-1:1234567890:ac4vomawb6/ESTestInvoke-stage/GET/"
    }
  ]
}
```
29. Click **Resources** and select **/hello**.
30. Select **GET** method and then **Method Request**.
31. In the **Settings** section expand the Authorization drop-down list to select the Lambda authorizer you just created, and then choose the check mark icon to save the choice. If your authorizer is not available, reload the page.
32. Click **Actions** and select **Deploy API**.
33. Select your stage and click **Deploy**.

Now you have GET API method with authorization.

34. Using your tool test both authorized and unathorized request.

Sample *curl* request to test the endpint without authorization token:

``
curl -s -X GET \
  'https://<URL OF YOUR API>' \
  -H 'Content-Type: application/json' \
  -H 'cache-control: no-cache'
``

And with authorization token sent to the endpoint:

``
curl -s -X GET \
  'https://<URL OF YOUR API>' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: thisismytokenvalue' \
  -H 'cache-control: no-cache'
``

## END LAB

<br><br>

<p align="right">&copy; 2020 Welastic Sp. z o.o.<p>
