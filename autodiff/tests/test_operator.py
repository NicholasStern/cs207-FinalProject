# This file serves to test the operator.py module
from ..operator import Operator as op
from ..autodiff import AutoDiff as ad
import numpy as np

x, z, n = tuple(ad.create_scalar([0, 1, 2048]))
v = ad.create_vector([[.9,.25,.5,.75]])[0]
orig_vals = np.copy(v._val)
y = 0


def test_sin():
    # Scalar
    sx = op.sin(x)
    assert np.sin(x._val) == sx._val
    for k in x._jacobian.keys():
        assert sx.partial(k) == x.partial(k) * np.cos(x._val)

    # Vector Values
    sv = op.sin(v)
    assert ~(np.sin(orig_vals) - sv._val).any()

    # Vector Jacobian
    for key in sv._dict.keys():
        assert ~(sv._dict[key] - v.getDerivative(key) * np.cos(v._val) * np.eye(len(v._val))).any()

    # Constant
    assert op.sin(y) == np.sin(y)


def test_cos():
    # Scalar
    cx = op.cos(x)
    assert np.cos(x._val) == cx._val
    for k in x._jacobian.keys():
        assert(cx.partial(k) == -x.partial(k) * np.sin(x._val))

    # Vector Values
    cv = op.cos(v)
    assert ~(np.cos(orig_vals) - cv._val).any()

    # Vector Jacobian
    for key in cv._dict.keys():
        assert ~(cv._dict[key] - v.getDerivative(key) * -np.sin(v._val) * np.eye(len(v._val))).any()

    # Constant
    assert op.cos(y) == np.cos(y)


def test_tan():
    # Scalar
    tx = op.tan(x)
    assert np.tan(x._val) == tx._val
    for k in x._jacobian.keys():
        assert tx.partial(k) == x.partial(k) * np.arccos(x._val)**2

    # Vector Values
    tv = op.tan(v)
    assert ~(np.tan(orig_vals) - tv._val).any()

    # Vector Jacobian
    for key in tv._dict.keys():
        assert ~(tv._dict[key] - v.getDerivative(key) * np.arccos(v._val)**2 * np.eye(len(v._val))).any()

    # Constant
    assert op.tan(y) == np.tan(y)


def test_arcsin():
    # Scalar
    asx = op.arcsin(x)
    assert np.arcsin(x._val) == asx._val
    for k in x._jacobian.keys():
        assert asx.partial(k) == -x.partial(k) * np.arcsin(x._val) \
               * np.arctan(x._val)

    # Vector Values
    asv = op.arcsin(v)
    assert ~(np.arcsin(orig_vals) - asv._val).any()

    # Vector Jacobian
    for key in asv._dict.keys():
        assert ~(asv._dict[key] - v.getDerivative(key) *-np.arcsin(v._val)*np.arctan(v._val) *
                 np.eye(len(v._val))).any()

    # Constant
    assert op.arcsin(y) == np.arcsin(y)


def test_arccos():
    # Scalar
    acx = op.arccos(x)
    assert np.arccos(x._val) == acx._val
    for k in x._jacobian.keys():
        assert acx.partial(k) == x.partial(k) * np.arccos(x._val) \
               * np.tan(x._val)

    # Vector Values
    acv = op.arccos(v)
    assert ~(np.arccos(orig_vals) - acv._val).any()

    # Vector Jacobian
    for key in acv._dict.keys():
        assert ~(acv._dict[key] - v.getDerivative(key) * np.arccos(v._val)*np.tan(v._val)*
                 np.eye(len(v._val))).any()

    # Constant
    assert op.arccos(y) == np.arccos(y)


def test_arctan():
    # Scalar
    atx = op.arctan(x)
    assert np.arctan(x._val) == atx._val
    for k in x._jacobian.keys():
        assert atx.partial(k) == -x.partial(k) * np.arcsin(x._val)**2

    # Vector Values
    atv = op.arctan(v)
    assert ~(np.arctan(orig_vals) - atv._val).any()

    # Vector Jacobian
    for key in atv._dict.keys():
        assert ~(atv._dict[key] - v.getDerivative(key) * -np.arcsin(v._val)**2 *
                 np.eye(len(v._val))).any()

    # Constant
    assert op.arctan(y) == np.arctan(y)


def test_sinh():
    # Scalar
    shx = op.sinh(x)
    assert np.sinh(x._val) == shx._val
    for k in x._jacobian.keys():
        assert shx.partial(k) == x.partial(k) * np.cosh(x._val)

    # Vector Values
    shv = op.sinh(v)
    assert ~(np.sinh(orig_vals) - shv._val).any()

    # Vector Jacobian
    for key in shv._dict.keys():
        assert ~(shv._dict[key] - v.getDerivative(key) * np.cosh(v._val) *
                 np.eye(len(v._val))).any()

    # Constant
    assert op.sinh(y) == np.sinh(y)


def test_cosh():
    # Scalar
    chx = op.cosh(x)
    assert np.cosh(x._val) == chx._val
    for k in x._jacobian.keys():
        assert chx.partial(k) == x.partial(k) * np.sinh(x._val)

    # Vector Values
    chv = op.cosh(v)
    assert ~(np.cosh(orig_vals) - chv._val).any()

    # Vector Jacobian
    for key in chv._dict.keys():
        assert ~(chv._dict[key] - v.getDerivative(key) * np.sinh(v._val) *
                 np.eye(len(v._val))).any()

    # Constant
    assert op.cosh(y) == np.cosh(y)


def test_tanh():
    # Scalar
    thx = op.tanh(x)
    assert np.tanh(x._val) == thx._val
    for k in x._jacobian.keys():
        assert thx.partial(k) == x.partial(k) * (1 - np.tanh(x._val)**2)

    # Vector Values
    thv = op.tanh(v)
    assert ~(np.tanh(orig_vals) - thv._val).any()

    # Vector Jacobian
    for key in thv._dict.keys():
        assert ~(thv._dict[key] - v.getDerivative(key) * (1-np.tanh(v._val)**2) *
                 np.eye(len(v._val))).any()

    # Constant
    assert op.tanh(y) == np.tanh(y)


def test_arcsinh():
    # Scalar
    ashx = op.arcsinh(x)
    assert np.arcsinh(x._val) == ashx._val
    for k in x._jacobian.keys():
        assert ashx.partial(k) == -x.partial(k) * np.arcsinh(x._val) \
               * np.arctanh(x._val)

    # Vector Values
    ashv = op.arcsinh(v)
    assert ~(np.arcsinh(orig_vals) - ashv._val).any()

    # Vector Jacobian
    for key in ashv._dict.keys():
        assert ~(ashv._dict[key] - v.getDerivative(key) * -np.arcsinh(v._val)*np.arctanh(v._val) *
                 np.eye(len(v._val))).any()
    # Constant
    assert op.arcsinh(y) == np.arcsinh(y)


def test_arccosh():
    x = ad.create_scalar(1)
    y = 2
    # Scalar
    achx = op.arccosh(x)
    assert np.arccosh(x._val) == achx._val
    for k in x._jacobian.keys():
        assert achx.partial(k) == -x.partial(k) * np.arccosh(x._val) \
               * np.tanh(x._val)

    # Vector Values
    v_temp = ad.create_vector([[1, 2, 3, 4]])[0]
    orig_temp = np.copy(v_temp._val)
    achv = op.arccosh(v_temp)
    assert ~(np.arccosh(orig_temp) - achv._val).any()

    # Vector Jacobian
    for key in achv._dict.keys():
        assert ~(achv._dict[key] - v_temp.getDerivative(key) * -np.arccosh(v_temp._val)*np.tanh(v_temp._val) *
                 np.eye(len(v_temp._val))).any()

    # Constant
    assert(op.arccosh(y) == np.arccosh(y))


def test_arctanh():
    # Scalar
    athx = op.arctanh(x)
    assert np.arctanh(x._val) == athx._val
    for k in x._jacobian.keys():
        assert athx.partial(k) == x.partial(k) * (1 - np.arctanh(x._val)**2)

    # Vector Values
    athv = op.arctanh(v)
    assert ~(np.arctanh(orig_vals) - athv._val).any()

    # Vector Jacobian
    for key in athv._dict.keys():
        assert ~(athv._dict[key] - v.getDerivative(key) * (1-np.arctanh(v._val)**2) *
                 np.eye(len(v._val))).any()

    # Constant
    assert op.arctanh(y) == np.arctanh(y)


def test_exp():
    # Scalar
    ex = op.exp(x)
    assert np.exp(x._val) == ex._val
    for k in x._jacobian.keys():
        assert ex.partial(k) == x.partial(k) * np.exp(x._val)

    # Vector Values
    ev = op.exp(v)
    assert ~(np.exp(orig_vals) - ev._val).any()

    # Vector Jacobian
    for key in ev._dict.keys():
        assert ~(ev._dict[key] - v.getDerivative(key) * np.exp(v._val) *
                 np.eye(len(v._val))).any()

    # Constant
    assert op.exp(y) == np.exp(y)


def test_log():
    # Scalar
    base = 10
    lgn = op.log(n, base)
    assert np.log(n._val) / np.log(base) == lgn._val
    for k in x._jacobian.keys():
        assert lgn.partial(k) == n.partial(k) / (n._val * np.log(base))

    # Vector Values
    lgv = op.log(v, base)
    assert ~(np.log(orig_vals) / np.log(base) - lgv._val).any()

    # Vector Jacobian
    for key in lgv._dict.keys():
        print(lgv._dict[key])
        print(v.getDerivative(key) / (v._val * np.log(base)) *
                 np.eye(len(v._val)))
        assert ~(lgv._dict[key] - v.getDerivative(key) / (v._val * np.log(base)) *
                 np.eye(len(v._val))).any()

    # Constant
    z = 24
    assert op.log(z, base) == np.log(z) / np.log(base)


def test_add():
    # Scalar
    res = op.sin(x) + op.sin(z)
    assert np.sin(x._val) + np.sin(z._val) == res._val
    for k in x._jacobian.keys():
        assert res.partial(k) == op.sin(x).partial(k) + op.sin(z).partial(k)

    # Constant
    assert op.sin(y) + op.sin(2 * y) == np.sin(y) + np.sin(2 * y)
