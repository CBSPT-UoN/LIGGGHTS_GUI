'''OpenGL extension ARB.program_interface_query

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.program_interface_query to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension provides a single unified set of query commands that can be
	used by applications to determine properties of various interfaces and
	resources used by program objects to communicate with application code,
	fixed-function OpenGL pipeline stages, and other programs.  In unextended
	OpenGL 4.2, there is a separate set of query commands for each different
	type of interface or resource used by the program.  These different sets
	of queries are structured nearly identically, but the queries for some
	interfaces have limited capability (e.g., there is no ability to enumerate
	fragment shader outputs).
	
	With the single set of query commands provided by this extension, a
	consistent set of queries is available for all interfaces, and a new
	interface can be added without having to introduce a completely new set of
	query commands.  These queries are intended to provide a superset of the
	capabilities provided by similar queries in OpenGL 4.2, and should allow
	for the deprecation of the existing queries.
	
	This extension defines two terms:  interfaces and active resources.  Each
	interface of a program object provides a way for the program to
	communicate with application code, fixed-function OpenGL pipeline stages,
	and other programs.  Examples of interfaces for a program object include
	inputs (receiving values from vertex attributes or outputs of other
	programs), outputs (sending values to other programs or per-fragment
	operations), uniforms (receiving values from API calls), uniform blocks
	(receiving values from bound buffer objects), subroutines and subroutine
	uniforms (receiving API calls to indicate functions to call during program
	execution), and atomic counter buffers (holding values to be manipulated
	by atomic counter shader functions).  Each interface of a program has a
	set of active resources used by the program.  For example, the resources
	of a program's input interface includes all active input variables used by
	the first stage of the program.  The resources of a program's uniform
	block interface consists of the set of uniform blocks with at least one
	member used by any shader in the program.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ARB/program_interface_query.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.ARB.program_interface_query import *
from OpenGL.raw.GL.ARB.program_interface_query import _EXTENSION_NAME

def glInitProgramInterfaceQueryARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

# INPUT glGetProgramInterfaceiv.params size not checked against 'pname'
glGetProgramInterfaceiv=wrapper.wrapper(glGetProgramInterfaceiv).setInputArraySize(
    'params', None
)
# INPUT glGetProgramResourceIndex.name size not checked against 'name'
glGetProgramResourceIndex=wrapper.wrapper(glGetProgramResourceIndex).setInputArraySize(
    'name', None
)
# INPUT glGetProgramResourceName.name size not checked against bufSize
glGetProgramResourceName=wrapper.wrapper(glGetProgramResourceName).setInputArraySize(
    'length', 1
).setInputArraySize(
    'name', None
)
# INPUT glGetProgramResourceiv.params size not checked against bufSize
# INPUT glGetProgramResourceiv.props size not checked against propCount
glGetProgramResourceiv=wrapper.wrapper(glGetProgramResourceiv).setInputArraySize(
    'length', 1
).setInputArraySize(
    'params', None
).setInputArraySize(
    'props', None
)
# INPUT glGetProgramResourceLocation.name size not checked against 'name'
glGetProgramResourceLocation=wrapper.wrapper(glGetProgramResourceLocation).setInputArraySize(
    'name', None
)
# INPUT glGetProgramResourceLocationIndex.name size not checked against 'name'
glGetProgramResourceLocationIndex=wrapper.wrapper(glGetProgramResourceLocationIndex).setInputArraySize(
    'name', None
)
### END AUTOGENERATED SECTION