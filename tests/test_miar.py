#!/usr/bin/env python


import sys
import os
from decimal import DivisionByZero

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from miar.measures import *

"""Tests for `miar` package."""

import pytest

@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string



def test_support_output():
    assert support([40,20,10,30]) == 0.4

def test_support_error():
    with pytest.raises(ZeroDivisionError):
        support([0,0,0,0])

def test_confidence_output():
    assert confidence([40,20,10,30]) == 4/6

def test_confidence_error():
    with pytest.raises(ZeroDivisionError):
        confidence([0,0,50,60])

def test_lift_output():
    assert lift([40,20,10,30]) == pytest.approx(1.333333)

def test_lift_error():
    with pytest.raises(ZeroDivisionError):
        lift([0,0,0,0])

def test_conviction_output():
    assert conviction([40,20,10,30]) == pytest.approx(1.499999999)

def test_conviction_error():
    with pytest.raises(ZeroDivisionError):
        conviction([0,0,0,0])

def test_leverage_output():
    assert leverage([40,20,10,30]) == pytest.approx(0.3666666)

def test_leverage_error():
    with pytest.raises(ZeroDivisionError):
        leverage([0,0,60,50])

def test_coverage_output():
    assert coverage([40,20,10,30]) == 0.6

def test_coverage_error():
    with pytest.raises(ZeroDivisionError):
        coverage([0,0,0,0])

def test_prevalence_output():
    assert prevalence([40,20,10,30]) == 0.5

def test_prevalence_error():
    with pytest.raises(ZeroDivisionError):
        prevalence([0,0,0,0])

def test_added_value_output():
    assert added_value([40,20,10,30]) == pytest.approx(0.16666666)

def test_added_value_error():
    with pytest.raises(ZeroDivisionError):
        added_value([0,0,0,0])

def test_recall_output():
    assert recall([40,20,10,30]) == 0.8

def test_recall_error():
    with pytest.raises(ZeroDivisionError):
        recall([0,50,0,100])

def test_bi_confidence_output():
    assert bi_confidence([40,20,10,30]) == pytest.approx(0.416666666)

def test_bi_confidence_error():
    with pytest.raises(ZeroDivisionError):
        bi_confidence([0,0,0,0])

def test_bi_lift_output():
    assert bi_lift([40,20,10,30]) == pytest.approx(2.6666666)

def test_bi_lift_error():
    with pytest.raises(ZeroDivisionError):
        bi_lift([0,0,0,0])

def test_bi_improve_output():
    assert bi_improve([40,20,10,30]) == pytest.approx(0.25000000)

def test_bi_improve_error():
    with pytest.raises(ZeroDivisionError):
        bi_improve([0,0,0,0])

def test_jaccard_output():
    assert jaccard([40,20,10,30]) == pytest.approx(0.57142857)

def test_jaccard_error():
    with pytest.raises(ZeroDivisionError):
        jaccard([0,0,0,0])

def test_one_way_support_output():
    assert one_way_support([40,20,10,30]) == pytest.approx(0.276691666)

def test_one_way_support_error():
    with pytest.raises(ZeroDivisionError):
        one_way_support([0,0,0,0])

def test_two_way_support_output():
    assert two_way_support([40,20,10,30]) == pytest.approx(0.166014999)

def test_two_way_support_error():
    with pytest.raises(ZeroDivisionError):
        two_way_support([0,0,0,0])

def test_support_causal_output():
    assert support_causal([40,20,10,30]) == 0.7

def test_support_causal_error():
    with pytest.raises(ZeroDivisionError):
        support_causal([0,0,0,0])

def test_confirm_descriptive_output():
    assert confirm_descriptive([40,20,10,30]) == 0.2

def test_confirm_descriptive_error():
    with pytest.raises(ZeroDivisionError):
        confirm_descriptive([0,0,0,0])

def test_confirm_causal_output():
    assert confirm_causal([40,20,10,30]) == pytest.approx(0.299999999)

def test_confirm_causal_error():
    with pytest.raises(ZeroDivisionError):
        confirm_causal([0,0,0,0])

def test_confidence_causal_output():
    assert confidence_causal([40,20,10,30]) == pytest.approx(0.63333333)

def test_confidence_causal_error():
    with pytest.raises(ZeroDivisionError):
        confidence_causal([0,0,50,70])

def test_confirmed_confidence_causal_output():
    assert confirmed_confidence_causal([40,20,10,30]) == 0.3

def test_confirmed_confidence_causal_error():
    with pytest.raises(ZeroDivisionError):
        confirmed_confidence_causal([0,0,50,70])

def test_confirmed_confidence_descriptive_output():
    assert confirmed_confidence_descriptive([40,20,10,30]) == pytest.approx(0.333333333)

def test_confirmed_confidence_descriptive_error():
    with pytest.raises(ZeroDivisionError):
        confirmed_confidence_descriptive([0,0,50,70])

def test_collective_strength_output():
    assert collective_strength([40,20,10,30]) == pytest.approx(2.333333333)

def test_collective_strength_error():
    with pytest.raises(ZeroDivisionError):
        collective_strength([0,0,0,0])

def test_j_measure_output():
    assert j_measure([40,20,10,30]) == pytest.approx(0.0490224995)

def test_j_measure_error():
    with pytest.raises(ZeroDivisionError):
        j_measure([0,0,0,0])

def test_certainty_factor_output():
    assert certainty_factor([40,20,10,30]) == pytest.approx(0.333333333)

def test_certainty_factory_error():
    with pytest.raises(ZeroDivisionError):
        certainty_factor([0,0,0,0])

def test_example_counterexample_rate_output():
    assert example_counterexample_rate([40,20,10,30]) == 0.5

def test_example_counterexample_rate_error():
    with pytest.raises(ZeroDivisionError):
        example_counterexample_rate([0,0,0,0])

def test_complement_class_support_output():
    assert complement_class_support([40,20,10,30]) == 0.4

def test_complement_class_support_error():
    with pytest.raises(ZeroDivisionError):
        complement_class_support([0,0,0,0])

def test_zhang_output():
    assert zhang([40,20,10,30]) == pytest.approx(0.5000000)

def test_zhang_error():
    with pytest.raises(ZeroDivisionError):
        zhang([0,0,0,0])

def test_chi_square_output():
    assert chi_square([40,20,10,30]) == pytest.approx(16.66666666)

def test_chi_square_error():
    with pytest.raises(ZeroDivisionError):
        chi_square([0,0,0,0])

def test_correlation_coefficient_output():
    assert correlation_coefficient([40,20,10,30]) == pytest.approx(0.40824829046)

def test_correlation_coefficient_error():
    with pytest.raises(ZeroDivisionError):
        correlation_coefficient([0,0,0,0])

def test_correlation_confidence_output():
    assert correlation_confidence([40,20,10,30]) == pytest.approx(0.2721655269)

def test_correlation_jaccard_output():
    assert correlation_jaccard([40,20,10,30]) == pytest.approx(0.233284737407)

def test_all_confidence_output():
    assert all_confidence([40,20,10,30]) == pytest.approx(0.66666666666)

def test_all_confidence_error():
    with pytest.raises(ZeroDivisionError):
        all_confidence([0,0,60,80])

def test_correlation_all_confidence_output():
    assert correlation_all_confidence([40,20,10,30]) == pytest.approx(0.2721655269)

def test_kappa_output():
    assert kappa([40,20,10,30]) == pytest.approx(0.399999999999)

def test_kappa_error():
    with pytest.raises(ZeroDivisionError):
        kappa([0,0,0,0])

def test_correlation_kappa_output():
    assert correlation_kappa([40,20,10,30]) == pytest.approx(0.163299316855)

def test_laplace_correction_output():
    assert laplace_correction([40,20,10,30]) == pytest.approx(0.66129032258)

def test_laplace_correction_error():
    with pytest.raises(ZeroDivisionError):
        laplace_correction([0,0,0,0])

def test_yule_q_output():
    assert yule_q([40,20,10,30]) == pytest.approx(0.714285714285)

def test_yule_q_error():
    with pytest.raises(ZeroDivisionError):
        yule_q([0,0,0,0])

def test_yule_y_output():
    assert yule_y([40,20,10,30]) == pytest.approx(0.420204102886)

def test_yule_y_error():
    with pytest.raises(ZeroDivisionError):
        yule_y([0,0,0,0])

def test_klosgen_output():
    assert klosgen([40,20,10,30]) == pytest.approx(0.105409255338)

def test_klosgen_error():
    with pytest.raises(ZeroDivisionError):
        klosgen([0,0,0,0])

def test_gini_index_output():
    assert gini_index([40,20,10,30]) == pytest.approx(0.0833333333)

def test_gini_index_error():
    with pytest.raises(ZeroDivisionError):
        gini_index([0,0,0,0])

def test_information_gain_output():
    assert information_gain([40,20,10,30]) == pytest.approx(0.4150374992)

def test_information_gain_error():
    with pytest.raises(ZeroDivisionError):
        information_gain([0,0,0,0])

def test_mutual_information_output():
    assert mutual_information([40,20,10,30]) == pytest.approx(0.12451124978)

def test_mutual_information_error():
    with pytest.raises(ZeroDivisionError):
        mutual_information([0,0,0,0])

def test_normalized_mutual_information_output():
    assert mutual_information([40,20,10,30]) == pytest.approx(0.12451124978)

def test_normalized_mutual_information_error():
    with pytest.raises(ZeroDivisionError):
        mutual_information([0,0,0,0])

def test_sebag_schoenauer_output():
    assert sebag_schoenauer([40,20,10,30]) == 2.0

def test_sebag_schoenauer_error():
    with pytest.raises(ZeroDivisionError):
        sebag_schoenauer([0,0,0,0])

def test_least_contradiction_output():
    assert least_contradiction([40,20,10,30]) == 0.4

def test_least_contradiction_error():
    with pytest.raises(ZeroDivisionError):
        least_contradiction([0,0,0,0])

def test_odd_multiplier_output():
    assert odd_multiplier([40,20,10,30]) == 2.0

def test_odd_multiplier_error():
    with pytest.raises(ZeroDivisionError):
        odd_multiplier([0,0,0,0])

def test_piatetsky_shapiro_output():
    assert piatetsky_shapiro([40,20,10,30]) == pytest.approx(0.1000000000)

def test_piatetsky_shapiro_error():
    with pytest.raises(ZeroDivisionError):
        piatetsky_shapiro([0,0,0,0])

def test_odds_ratio_output():
    assert odds_ratio([40,20,10,30]) == pytest.approx(5.99999999)

def test_odds_ratio_error():
    with pytest.raises(ZeroDivisionError):
        odds_ratio([0,0,0,0])

def test_validity_output():
    assert validity([40,20,10,30]) == pytest.approx(0.30000000)

def test_validity_error():
    with pytest.raises(ZeroDivisionError):
        validity([0,0,0,0])

def test_kulczynski_1_output():
    assert kulczynski_1([40,20,10,30]) == pytest.approx(1.33333333)

def test_kulczynksi_1_error():
    with pytest.raises(ZeroDivisionError):
        kulczynski_1([0,0,0,0])

def test_kulczynski_2_output():
    assert kulczynski_2([40,20,10,30]) == pytest.approx(0.733333333)

def test_kulczynksi_2_error():
    with pytest.raises(ZeroDivisionError):
        kulczynski_2([0,0,0,0])

def test_conditional_entropy_output():
    assert conditional_entropy([40,20,10,30]) == pytest.approx(0.918295834054)

def test_conditional_entropy_error():
    with pytest.raises(ZeroDivisionError):
        conditional_entropy([0,0,50,80])

def test_theil_uncertainty_coefficient_output():
    assert theil_uncertainty_coefficient([40,20,10,30]) == pytest.approx(0.124511249783)

def test_theil_uncertainty_coefficient_error():
    with pytest.raises(ZeroDivisionError):
        theil_uncertainty_coefficient([0,0,0,0])
