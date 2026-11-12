local Widget = require "widgets/widget"
local Image = require "widgets/image"
local Text = require "widgets/text"

local WIDTH = 660
local HEIGHT = 14
local SEGMENTS = 33

local AgeBar = Class(Widget, function(self, owner, inventory)
    Widget._ctor(self, "WandaAgeBar")
    self.owner = owner
    self.inventory = inventory
    self:SetClickable(false)

    local background = self:AddChild(Image("images/ui.xml", "white.tex"))
    background:SetSize(WIDTH + 8, HEIGHT + 8)
    background:SetTint(.04, .04, .04, .88)
    self.segments = {}
    for i = 1, SEGMENTS do
        local t = (i - .5) / SEGMENTS
        local segment = self:AddChild(Image("images/ui.xml", "white.tex"))
        segment:SetSize(WIDTH / SEGMENTS + .5, HEIGHT)
        segment:SetPosition(-WIDTH / 2 + WIDTH * t, 0)
        segment:SetTint(1 - .55 * t, .20 + .53 * t, .14 + .18 * t, .9)
        self.segments[i] = segment
    end
    self.marker = self:AddChild(Image("images/ui.xml", "white.tex"))
    self.marker:SetSize(5, HEIGHT + 16)
    self.marker:SetTint(1, 1, 1, 1)
    self.age = self:AddChild(Text(NUMBERFONT, 27))
    self.age:SetPosition(0, 26)
    self.age:SetColour(1, 1, 1, 1)
    self:StartUpdating()
end)

function AgeBar:OnUpdate()
    local owner = self.owner
    local health = owner.replica ~= nil and owner.replica.health or nil
    if owner:HasTag("playerghost") or health == nil then
        self:Hide()
        return
    end
    self:Show()
    local percent = math.max(0, math.min(1, health:GetPercent()))
    self.marker:SetPosition(-WIDTH / 2 + WIDTH * percent, 0)
    local tuning = TUNING
    local years = tuning.WANDA_MIN_YEARS_OLD + (1 - percent) * (tuning.WANDA_MAX_YEARS_OLD - tuning.WANDA_MIN_YEARS_OLD)
    self.age:SetString(tostring(math.floor(years + .5)))
    local top = self.inventory.toprow
    local y = top ~= nil and top:GetPosition().y or 0
    self:SetPosition(0, y + 78)
end

return AgeBar
