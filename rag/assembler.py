def assemble(contexts: dict):
    final = ""
    for k, v in contexts.items():
        final += f"\n[{k.upper()}]\n{v}\n"
    return final
