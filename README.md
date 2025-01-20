## Harvard Computer System Group 

### Repo structures
```
img/ : images
srcripts/ : scripts to generate the html code
index_base.html : html template
```

### How to generate the html code
Python dependencies: `requests`, `bs4` can be installed using `pip3 install requests bs4`.
Run the following script which will crawl the website and generate the html code. 

```
python3 scripts/main.py
```

### Automatic update
The html code is automatically updated at GitHub push and every week using a cron job on Cloudflare. 
Alternatively, we can use `curl -X POST "https://api.cloudflare.com/client/v4/pages/webhooks/deploy_hooks/415b5228-db71-44d6-9eea-6dab333d5921"` to trigger the update.



