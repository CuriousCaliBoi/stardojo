using StardewModdingAPI;
using ActionSpace.actions;
using System;
using System.IO;

namespace InitTask
{
    /// <summary>
    /// Simple API wrapper for task initialization and observation methods
    /// </summary>
    public static class InitTaskAPI
    {
        /// <summary>
        /// Observe the game state and return as byte array (CBOR encoded)
        /// </summary>
        public static byte[]? observe(string size, Mod mod)
        {
            int sizeInt = int.Parse(size);
            return Actions.ExportGameData(sizeInt, mod);
        }

        /// <summary>
        /// Observe the game state and return as JSON string
        /// </summary>
        public static string observe_v2(string size, Mod mod)
        {
            int sizeInt = int.Parse(size);
            return Actions.ExportGameData_v2(sizeInt, mod);
        }

        /// <summary>
        /// Get surroundings data
        /// </summary>
        public static System.Collections.Generic.List<Actions.TileInfo> get_surroundings(string size, Mod mod)
        {
            int sizeInt = int.Parse(size);
            return Actions.GetSurroundings(sizeInt);
        }

        /// <summary>
        /// Load game record (placeholder - implement based on your needs)
        /// </summary>
        public static string? load_game_record(string savePath, Mod mod)
        {
            // TODO: Implement game loading logic if needed
            mod.Monitor.Log($"load_game_record called with path: {savePath}", LogLevel.Info);
            return null;
        }

        /// <summary>
        /// Pause the game
        /// </summary>
        public static void pause(Mod mod)
        {
            StardewValley.Game1.paused = true;
        }

        /// <summary>
        /// Resume the game
        /// </summary>
        public static void resume(Mod mod)
        {
            StardewValley.Game1.paused = false;
        }
    }
}
