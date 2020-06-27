package main

import "gopkg.in/macaron.v1"

func main() {
    m := macaron.Classic()
    m.Get("/", HomepageHandler) 
        
    
    m.Run()
}


// NotFoundHandler handles 404 errors
func NotFoundHandler(ctx *macaron.Context) {
	ctx.HTML(http.StatusNotFound, "notfound")
}

// DevicesHandler handles the devices page
func HomepageHandler(ctx *macaron.Context) {
	ctx.Data["PageTitle"] = ""
	ctx.HTML(http.StatusOK, "home")
}