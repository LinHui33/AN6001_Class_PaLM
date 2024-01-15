#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask,request,render_template
import google.generativeai as palm


# In[ ]:


app = Flask(__name__)
palm.configure(api_key = "AIzaSyA0e7cWUqgDlkDUpNosPn7BqZoTZhXpUDw")
defaults = { "model": "models/chat-bison-001"}


# In[ ]:


@app.route("/",methods = ["GET","POST"])
def index():
    if request.method == "POST":
        qn = request.form.get('qn')
        response = palm.chat(**defaults,messages=qn)
        return render_template("index.html", result = response.last)
    else:
        return render_template("index.html", result = "Waiting for Question.............")


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:




