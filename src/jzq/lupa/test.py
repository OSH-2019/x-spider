import lupa
from lupa import LuaRuntime

lua = LuaRuntime(unpack_returned_tuples=True)

print(lua.eval('1+1')) # output: 2
lua_func = lua.eval('function(f, n) return f(n) end')

def py_add1(n): 
    return n+1

print(lua_func(py_add1, 2)) # output: 3

print(lua.eval('python.eval(" 2 ** 2 ")') == 4) # output: True

print(lua.eval('python.builtins.str(4)') == '4') # output: True

# lua_type(obj) 函数用于输出 type of a wrapped Lua object
print(lupa.lua_type(lua_func)) # output: 'function'
print(lupa.lua_type(lua.eval('{}')))# output: 'table'
print(lupa.lua_type(123) is None) # output: True
print(lupa.lua_type('abc') is None) # output: True
print(lupa.lua_type({}) is None) # output: True

# flag unpack_returned_tuples=True that is passed to create the Lua runtime
lua.execute('a,b,c = python.eval("(1,2)")')
g = lua.globals()
print(g.a)   # output: 1
print(g.b)   # output: 2
print(g.c is None)   # output: True

# flag unpack_returned_tuples=False, functions that return a tuple pass it through to the Lua code
non_explode_lua = lupa.LuaRuntime(unpack_returned_tuples=False)
non_explode_lua.execute('a,b,c = python.eval("(1,2)")')
g = non_explode_lua.globals()
print(g.a)   # output: (1, 2)
g.b is None  # output: True
g.c is None  # output: True
