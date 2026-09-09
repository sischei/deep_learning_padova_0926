#!/usr/bin/env bash
# Execute the CPU-light notebooks in a scratch copy and report pass/fail.
cd "$(dirname "$0")"
OUT=/tmp/padova_smoke; rm -rf $OUT; mkdir -p $OUT
NBS="
day1/code/01_deep_learning_intro/01_01_BasicML_intro.ipynb
day1/code/01_deep_learning_intro/01_02_GradientDescent_and_StochasticGradientDescent.ipynb
day1/code/01_deep_learning_intro/01_03_Double_Descent.ipynb
day1/code/01_deep_learning_intro/01_05_PyTorch_intro.ipynb
day1/code/02_deep_equilibrium_nets/02_01_Brock_Mirman_1972_DEQN.ipynb
day1/code/02_deep_equilibrium_nets/02_02_Brock_Mirman_Uncertainty_DEQN.ipynb
day2/code/06_surrogates_and_gps/06_02_GP_Regression.ipynb
day2/code/07_structural_estimation/07_01_SMM_One_Parameter.ipynb
day2/code/08_pinns/08_01_ODE_PINN_ZeroBCs.ipynb
day2/code/08_pinns/08_02_ODE_PINN_SoftVsHardBCs.ipynb
day2/code/09_pinns_applications/09_01_Cake_Eating_HJB_PINN.ipynb
day2/code/09_pinns_applications/09_04_PINN_Exercise.ipynb
"
for nb in $NBS; do
  name=$(basename "$nb" .ipynb)
  # run in the notebook's own directory so relative data files resolve
  timeout 1800 python3 -m nbconvert --to notebook --execute \
      --ExecutePreprocessor.timeout=900 \
      --output "$OUT/$name.ipynb" "$nb" >"$OUT/$name.log" 2>&1
  rc=$?
  [ $rc -eq 0 ] && echo "PASS  $name" || echo "FAIL  $name (rc=$rc)"
done
