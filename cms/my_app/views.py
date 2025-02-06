def homepge(request):
    ret = '''
    <!DOCTYPE html>
    <html>
    <head></head>
    <body>
    <h1>Homepage</h1>
    </body></html>
    '''
    return HttpResponse(ret)

def hello(request):
    return HttpResponse('Ahoj!')