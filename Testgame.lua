local tbl = {name = "Lua专属测试表", data = {10, 20, 30}}

-- Lua独有的for in pairs迭代器
for key, val in pairs(tbl.data) do
    local calc = val ^ 2 -- Lua原生幂运算符号^
    tbl[key] = calc
end

-- Lua独有的元表metatable
local mt = {
    __index = function(t, k)
        return "不存在键:" .. tostring(k)
    end,
    __newindex = function(t, k, v)
        rawset(t, k, "锁定:" .. v)
    end
}
setmetatable(tbl, mt)

local function sum(...)
    local total = 0
    for _, num in ipairs{...} do
        total = total + num
    end
    return total
end

-- 协程 coroutine，Lua标志性独有功能
local co = coroutine.create(function()
    coroutine.yield(sum(5, 15, 25))
    coroutine.yield(sum(10, 20))
end)
local _, co_res1 = coroutine.resume(co)
local _, co_res2 = coroutine.resume(co)

print("协程结果1:" .. co_res1)
print("协程结果2:" .. co_res2)
local function outer(x)
    return function(y)
        return x * y
    end
end
local mulFunc = outer(8)
local finalVal = mulFunc(7)

