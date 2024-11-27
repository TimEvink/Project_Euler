import importlib

# Entry point for loading solutions.


def runsolution(n): # Imports the solution file corresponding to the integer n
	modulename = f"Project_Euler.P{n:03d}.s{n:03d}" # Generates the path as string
	try:
		return importlib.import_module(modulename) #imports the solution file
	except ModuleNotFoundError:
		print(f"Module '{modulename}' does not exist.")
	except Exception as e:
		print(f"An error occurred: {e}")

# To run for example the solution of problem 96, simply run this file by uncommenting the following

#runsolution(96)