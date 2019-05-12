
function test1(params)
    return 'test1:'..params
end
 
function test2(params)
    return 'test2:'..test1(params)
end
 
-- 入口函数,实现反射函数调用
function functionCall(func_name,params)
    local is_true,result
    local sandBox = function(func_name,params)
        local result
        result = _G[func_name](params)
        return result
    end
    is_true,result= pcall(sandBox,func_name,params)
    return result
end
