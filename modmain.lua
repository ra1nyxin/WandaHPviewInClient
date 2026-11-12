local AgeBar = require "widgets/wanda_age_bar"

AddClassPostConstruct("widgets/inventorybar", function(inventory)
    if inventory.owner ~= nil and inventory.owner.prefab == "wanda" and inventory.root ~= nil then
        inventory.root:AddChild(AgeBar(inventory.owner, inventory))
    end
end)
