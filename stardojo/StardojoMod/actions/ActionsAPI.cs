using StardewModdingAPI;
using StardewValley;
using ActionSpace.actions;

namespace ActionSpace.actions
{
    /// <summary>
    /// Simple API wrapper for Actions class methods
    /// </summary>
    public static class ActionsAPI
    {
        // Movement
        public static async System.Threading.Tasks.Task<bool> move(string direction, Mod mod)
        {
            return await Actions.move(direction, mod);
        }

        // Actions
        public static void turn(string direction, Mod mod)
        {
            Actions.turn(direction, mod);
        }

        public static void interact(Mod mod)
        {
            Actions.interact(mod);
        }

        public static void use(Mod mod)
        {
            Actions.use(mod);
        }

        public static void leftClick(string x, string y, Mod mod)
        {
            Actions.leftClick(x, y, mod);
        }

        public static void rightClick(string x, string y, Mod mod)
        {
            Actions.rightClick(x, y, mod);
        }

        // Tools and items
        public static void use_tool(string posX, string posY, Mod mod)
        {
            int x = int.Parse(posX);
            int y = int.Parse(posY);
            Actions.use_tool(x, y, mod);
        }

        public static void use_item(string posX, string posY, Mod mod)
        {
            int x = int.Parse(posX);
            int y = int.Parse(posY);
            Actions.use_item(x, y, mod);
        }

        public static void place_item(string posX, string posY, Mod mod)
        {
            int x = int.Parse(posX);
            int y = int.Parse(posY);
            Actions.place_item(x, y, mod);
        }

        public static void eat_food(Mod mod)
        {
            Actions.eat_food(mod);
        }

        public static void drop_in(string itemIndex, Mod mod)
        {
            int index = int.Parse(itemIndex);
            var item = Game1.player.Items[index];
            if (item != null)
            {
                Actions.drop_in(item, mod);
            }
        }

        public static void attach(string itemIndex, Mod mod)
        {
            int index = int.Parse(itemIndex);
            var item = Game1.player.Items[index];
            if (item is StardewValley.Object obj)
            {
                Actions.attach(obj, mod);
            }
        }

        public static void detach(Mod mod)
        {
            Actions.detach(mod);
        }

        public static void FireSlingshot(string posX, string posY, Mod mod)
        {
            int x = int.Parse(posX);
            int y = int.Parse(posY);
            Actions.FireSlingshot(x, y, mod);
        }

        // Crafting
        public static void craft(string item, Mod mod)
        {
            Actions.craft(item, mod);
        }

        // Shops
        public static void open_shop(string shopId, string ownerName, Mod mod)
        {
            Actions.open_shop(shopId, ownerName, mod);
        }

        public static void close_shop(string shopId, string ownerName, Mod mod)
        {
            Actions.close_shop(shopId, ownerName, mod);
        }

        public static void buy_from_shop(string index, string count, Mod mod)
        {
            int idx = int.Parse(index);
            int cnt = int.Parse(count);
            Actions.buy_from_shop(idx, cnt, mod);
        }

        public static void sell_to_shop(Mod mod)
        {
            Actions.sell_to_shop(mod);
        }

        public static void buy_from_animals_shop(string index, string building_index, string animal_name, Mod mod)
        {
            int idx = int.Parse(index);
            int bIdx = int.Parse(building_index);
            Actions.buy_from_animals_shop(idx, bIdx, animal_name, mod);
        }

        // Dialogue and menus
        public static void select_dialogue(string index, Mod mod)
        {
            int idx = int.Parse(index);
            Actions.select_dialogue(idx, mod);
        }

        public static void answer_question(string answerKey, string[] questionKeys, Mod mod)
        {
            Actions.answer_question(answerKey, questionKeys);
        }

        public static void exit_menu(Mod mod)
        {
            Actions.exit_menu();
        }

        // Building and upgrades
        public static void open_carpenter_construct(Mod mod)
        {
            Actions.open_carpenter_construct();
        }

        public static void build_current_building(string x_bias, string y_bias, Mod mod)
        {
            int x = int.Parse(x_bias);
            int y = int.Parse(y_bias);
            Actions.build_current_building(x, y);
        }

        public static void upgrade_backpack(Mod mod)
        {
            Actions.upgrade_backpack();
        }

        public static void upgrade_house(Mod mod)
        {
            Actions.upgrade_house();
        }

        // NPCs
        public static void talk(Mod mod)
        {
            Actions.talk(mod);
        }

        public static void location_perform_action(string actionId, Mod mod)
        {
            Actions.location_perform_action(actionId);
        }

        // Special interactions
        public static void InteractWithObject(string posX, string posY, Mod mod)
        {
            int x = int.Parse(posX);
            int y = int.Parse(posY);
            Actions.InteractWithObject(new Microsoft.Xna.Framework.Vector2(x, y), mod);
        }

        public static void InteractWithChest(StardewValley.Objects.Chest chest, Mod mod)
        {
            Actions.InteractWithChest(chest, mod);
        }

        public static void InteractWithBed(Mod mod)
        {
            Actions.InteractWithBed(mod);
        }

        public static void WatchTV(Mod mod)
        {
            Actions.WatchTV(mod);
        }

        public static void PlayArcade(Mod mod)
        {
            Actions.PlayArcade(mod);
        }

        public static void UseMineElevator(Mod mod)
        {
            Actions.UseMineElevator(mod);
        }

        public static void UseSlotMachine(Mod mod)
        {
            Actions.UseSlotMachine(mod);
        }
    }
}
