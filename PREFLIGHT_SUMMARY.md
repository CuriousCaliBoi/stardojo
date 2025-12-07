# Pre-Flight Check Summary

## ✅ All Critical Issues Fixed

### 1. **Import Errors** ✓
- Fixed `read_resource_file` to handle absolute paths
- Fixed `log_processor` import path
- Fixed `utils` import conflict
- Fixed `stardew_env` dotenv loading
- Added missing imports (`time`, `atexit`)

### 2. **Path Resolution** ✓
- Fixed config file paths (changed from `./conf/` to `agent/conf/`)
- Fixed resource file path checking
- All paths now resolve correctly relative to project root

### 3. **Error Handling** ✓
- Added validation for `STARDEW_APP_PATH` (raises clear error if missing)
- Added validation for memory mapped file (waits for it to be created)
- Added timeout and error handling for `wait_for_server`
- Added error handling for task loading (validates task_id range)
- Added error handling for API key (raises clear error if missing)
- Added error handling for game data files
- Added error handling for task evaluation

### 4. **Connection Issues** ✓
- `wait_for_server` now raises `ConnectionError` with helpful message
- Memory mapped file waits up to 30s before failing
- Better error messages for connection failures

### 5. **Code Quality** ✓
- Fixed syntax warning in `actions.py` (invalid escape sequence)
- Improved error messages throughout
- Added startup information display

## 🔍 Pre-Flight Check

Run this before starting the agent:

```bash
cd /Users/princezuk0/projects/stardojo
python preflight_check.py
```

This will check:
- ✅ Environment variables (STARDEW_APP_PATH, OA_OPENAI_KEY)
- ✅ Game server connection (port 10783)
- ✅ Memory mapped file existence
- ✅ All configuration files
- ✅ Task files
- ✅ Resource files
- ✅ Game data files
- ✅ Critical imports
- ✅ Module paths

## 🚀 Running the Agent

**Prerequisites:**
1. Stardew Valley must be running with the mod loaded
2. Game should be loaded (not at title screen) if using `--new_game False`
3. Mod should be listening on port 10783 (or specify with `--port`)

**Command:**
```bash
python env/llm_env.py --port 10783 --task_name farming_lite --task_id 0
```

## ⚠️ Common Issues & Solutions

### Issue: "Game server not listening on port 10783"
**Solution:** 
- Make sure Stardew Valley is running
- Check SMAPI console for mod errors
- Verify mod is loaded (should see "StardojoMod" in SMAPI output)

### Issue: "OA_OPENAI_KEY not set"
**Solution:**
- Add to `env/.env`: `OA_OPENAI_KEY=sk-your-key-here`
- Or export in shell: `export OA_OPENAI_KEY=sk-your-key-here`

### Issue: "Memory mapped file not found"
**Solution:**
- The file is created when the mod starts
- Make sure the game is running and mod is loaded
- Check that port matches (default 10783)

### Issue: "Task ID out of range"
**Solution:**
- Check available tasks: `python -c "import yaml; print(list(yaml.safe_load(open('env/tasks/task_suite/farming_lite.yaml')).keys()))"`
- Use a valid task_id (0 to N-1)

## 📝 Notes

- The mod must be rebuilt after code changes (C# is compiled)
- Use `reload` in SMAPI console to reload mods without restarting
- For Harmony patches, a full game restart may be needed
- Port 10783 is the default - change with `--port-id` when launching SMAPI
