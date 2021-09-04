A Closure is a function object that remembers values in enclosing scopes even if they are not present in memory.    

-   It is a record that stores a function together with an environment: a mapping associating each free variable of the function (variables that are used locally but defined in an enclosing scope) with the value or reference to which the name was bound when the closure was created.
-   A closure—unlike a plain function—allows the function to access those captured variables through the closure’s copies of their values or references, even when the function is invoked outside their scope.

```python
def outerFunction(text):
    text = text

    def innerFunction():
	    print(text)

	# Note we are returning function
	# WITHOUT parenthesis
	return innerFunction 

if __name__ =`= '__main__':
	 myFunction = outerFunction(`'Hey!')
	 myFunction()
 ```
 
 
 1.  As observed from the above code, closures help to invoke functions outside their scope.
2.  The function **innerFunction** has its scope only inside the outerFunction. But with the use of closures, we can easily extend its scope to invoke a function outside its scope.