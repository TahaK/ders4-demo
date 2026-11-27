# PreToolUse hook: Bash komutunda "rm " varsa engelle (çıkış kodu 2 = engelle, stderr modele gider)
import json, sys
girdi = json.load(sys.stdin)
komut = girdi.get("tool_input", {}).get("command", "")
if "rm " in komut or komut.strip().startswith("rm"):
    print("Bu demoda dosya silmek yasak (hook tarafından engellendi).", file=sys.stderr)
    sys.exit(2)
sys.exit(0)
