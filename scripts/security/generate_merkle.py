import hashlib
import os
import json

def get_file_hash(filepath):
    sha256_hash = hashlib.sha256()
    with open(filepath, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def build_merkle_tree(hashes):
    if len(hashes) == 0:
        return None
    if len(hashes) == 1:
        return hashes[0]

    new_hashes = []
    for i in range(0, len(hashes), 2):
        if i + 1 < len(hashes):
            combined = hashes[i] + hashes[i+1]
        else:
            combined = hashes[i] + hashes[i] # Duplicate last hash if odd
        new_hashes.append(hashlib.sha256(combined.encode()).hexdigest())

    return build_merkle_tree(new_hashes)

def main():
    exclude_dirs = {'.git', '.github', '__pycache__', 'node_modules', 'verification'}
    exclude_files = {'checksums.sha256', 'checksums.sha512', 'manifest.merkle', 'test_results.log', 'pytest.log', 'install.log'}

    file_hashes = {}
    for root, dirs, files in os.walk('.'):
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        for file in sorted(files):
            if file in exclude_files:
                continue
            path = os.path.join(root, file)
            file_hashes[path] = get_file_hash(path)

    sorted_paths = sorted(file_hashes.keys())
    leaf_hashes = [file_hashes[p] for p in sorted_paths]

    root_hash = build_merkle_tree(leaf_hashes)

    manifest = {
        "root_hash": root_hash,
        "algorithm": "SHA256",
        "leaves": file_hashes
    }

    with open('manifest.merkle', 'w') as f:
        f.write("# Merkle Manifest\n\n")
        f.write(f"- Root Hash: {root_hash}\n")
        f.write("- Algorithm: SHA256\n\n")
        f.write("## File Hashes (Leaves)\n")
        for path in sorted_paths:
            f.write(f"- {path}: {file_hashes[path]}\n")

if __name__ == "__main__":
    main()
