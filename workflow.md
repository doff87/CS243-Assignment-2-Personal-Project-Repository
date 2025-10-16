Git Workflow Documentation



Repository Setup

I set up the repository fairly standard at first. Initiate on the GitHub site, git init the repository, and make a commit. Mine likely differs from others in that

after doing that I made my assignment repository a submodule of my class repository. I would prefer in most cases just to have it as a monorepository and subfolders

but this does allow for separate projects to have their own venvs and versioning in git that wouldn't be possible with a single repository.



Commit History Summary

90eef4b (HEAD -> main, origin/main) Add third function. Utility tool complete.

3e041aa Second function added

82faad4 Adding pyfiglet installation to requirements.txt

347f400 Add first function. Input validation functions added.

a2f9db9 Add first function (measurementConverter) and match case for selection

b009d45 Add .gitignore

b2f4436 Creation of Python Utility Tool python file

5542a18 Initial commit with project structure



Most Challenging Commit

It's between 347f00 and a2f9db9. It's a function of it being my first python code in a long while along with having made the first function FAR too ambitious and having to

write my validation functions during that time. Once I narrowed my scope it became a bit more manageable, but multiple functions with that many branches and validations would

have taken substantially longer to compelte.



What I Learned

I learned to become far more comfortable with creating, initializing, committing, and pushing a GitHub repository. On top of that, I learned the pros and cons of using a 

git submodule as opposed to a singular monorepository. Finally, learning how to set up and view a submodule is also quite useful information.



1. Match/Case - It is similar to switch for Java. This is essential for avoiding a complete mess of if/elif/else statements
2. def - To define a function, and honestly I could have used it more. The more modular your code is the more stable it becomes and it becomes substantially easier to learn to a new coder as well as diagnose any issues as they are isolated to singular small functions as opposed to large complex functions.
3. while True - this is more referring to looping. While doing data validation being able to loop back is essential to prevent the user from having to continually restart the program. It also allows for the user to designate when they would like to exit the program.
