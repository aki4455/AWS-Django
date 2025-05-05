# AWS-Django
'''1. S3 Bucket Setup:
Created an S3 bucket (akmalllbucket).
Uploaded templates (e.g., album_list.html, album_create.html) into the templates folder inside the S3 bucket.
2. Configured AWS Credentials:
Configured AWS access credentials (AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY) in Django settings using boto3 (the AWS SDK for Python).
Set AWS_S3_BUCKET_NAME and other necessary parameters like AWS_S3_REGION_NAME.
3. Django Configuration for S3 Templates:
Modified Django settings to use S3 for serving templates:
Set TEMPLATES['DIRS'] to point to the S3 URL (https://akmalllbucket.s3.amazonaws.com/templates/).
Ensured that APP_DIRS is set to False (so Django doesnt search for templates locally).
Configured Django to use django.template.backends.django.DjangoTemplates for loading templates from S3.
4. Permissions on S3:
Ensured that the S3 bucket and its templates folder are publicly accessible so that 
Django can fetch the templates from the bucket. We discussed setting a public read policy for the templates/ folder in S3.
5. S3 Template URL Access:
Verified that templates like album_list.html are 
accessible through direct URLs like https://akmalllbucket.s3.amazonaws.com/templates/album_list.html.
The project involves setting up a Django application with the goal of making HTML files accessible through 
Amazon S3. 
Initially, Django was configured and set up on a local machine, with a focus on using the app album for managing albums, which includes various views and templates. 
The goal was to allow users to view album data and interact with the application through the web interface.

Following the initial Django setup, the HTML files associated with the album app were transferred to an Amazon S3 bucket to ensure scalability and easy access. 
The connection between Django and S3 was established by installing the necessary libraries (boto3 and django-storages) and configuring the settings.py file
to use S3 for static and media file storage. 
This allows HTML files, images, and other static files to be served from S3, reducing the load on the web server and improving 
the performance and availability of the application.

By using Amazon S3 for static file storage, the project ensures that files 
can be accessed easily, even if the Django application is hosted on an EC2 instance,
 without the need for a dedicated 
static file server. Additionally, this approach makes it easier to scale the application, as S3 
handles the file distribution and availability across regions. The integration with S3 is a key aspect of 
ensuring that static files are efficiently managed while keeping the 
Django application focused on dynamic content and functionality.
'''
