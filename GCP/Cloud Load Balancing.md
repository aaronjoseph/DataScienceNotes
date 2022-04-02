- This allows for single front-end to the world
- Users get a single, global anycast IP address
- Traffic goes over the Google backbone from the closest point of presense to the user
- Backends are selected based on load
- Only healthy backends receive traffic
- No pre-warming is required

Traffic that it can handle 
- HTTP, HTTPS
- TCP 
- SSL
- UDP