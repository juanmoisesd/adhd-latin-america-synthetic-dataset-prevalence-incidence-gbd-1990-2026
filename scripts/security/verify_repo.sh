#!/bin/bash
set -e

echo "=== ADHD Dataset Integrity Verification ==="

echo "[1/3] Verifying SHA256 Checksums..."
sha256sum -c checksums.sha256 --quiet || { echo "SHA256 verification failed!"; exit 1; }
echo "✓ SHA256 Checksums OK"

echo "[2/3] Verifying SHA512 Checksums..."
sha512sum -c checksums.sha512 --quiet || { echo "SHA512 verification failed!"; exit 1; }
echo "✓ SHA512 Checksums OK"

echo "[3/3] Verifying Merkle Root..."
# Run the merkle generation script and check if the root matches the manifest
CURRENT_ROOT=$(python3 scripts/security/generate_merkle.py && grep "Root Hash:" manifest.merkle | cut -d ' ' -f 4)
MANIFEST_ROOT=$(grep "Root Hash:" manifest.merkle | cut -d ' ' -f 4)

if [ "$CURRENT_ROOT" == "$MANIFEST_ROOT" ]; then
    echo "✓ Merkle Root Verified: $CURRENT_ROOT"
else
    echo "✗ Merkle Root Mismatch!"
    echo "  Expected: $MANIFEST_ROOT"
    echo "  Got:      $CURRENT_ROOT"
    exit 1
fi

echo "==========================================="
echo "ALL INTEGRITY CHECKS PASSED"
