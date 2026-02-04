import 'package:flet/flet.dart';
import 'package:flutter/material.dart';
import 'package:flutter_spinkit/flutter_spinkit.dart';

class FletSpinkitControl extends StatelessWidget {
  final Control control;

  const FletSpinkitControl({
    super.key,
    required this.control,
  });

  @override
  Widget build(BuildContext context) {
    // getString is used here as you requested
    String type = control.getString("type") ?? "RotatingCircle";
    Color color = control.getColor("color", context) ?? Colors.white;
    double size = control.getDouble("size") ?? 100.0;

    Widget myControl;

    switch (type.toLowerCase()) {
      case "wave": myControl = SpinKitWave(color: color, size: size); break;
      case "doublebounce": myControl = SpinKitDoubleBounce(color: color, size: size); break;
      case "threebounce": myControl = SpinKitThreeBounce(color: color, size: size); break;
      case "fadingcircle": myControl = SpinKitFadingCircle(color: color, size: size); break;
      case "pulse": myControl = SpinKitPulse(color: color, size: size); break;
      case "cubegrid": myControl = SpinKitCubeGrid(color: color, size: size); break;
      case "chasingdots": myControl = SpinKitChasingDots(color: color, size: size); break;
      case "rotatingplain": myControl = SpinKitRotatingPlain(color: color, size: size); break;
      case "wanderingcubes": myControl = SpinKitWanderingCubes(color: color, size: size); break;
      case "fadingfour": myControl = SpinKitFadingFour(color: color, size: size); break;
      case "fadingcube": myControl = SpinKitFadingCube(color: color, size: size); break;
      case "circle": myControl = SpinKitCircle(color: color, size: size); break;
      case "foldingcube": myControl = SpinKitFoldingCube(color: color, size: size); break;
      case "pumpingheart": myControl = SpinKitPumpingHeart(color: color, size: size); break;
      case "hourglass": myControl = SpinKitHourGlass(color: color, size: size); break;
      case "pouringhourglass": myControl = SpinKitPouringHourGlass(color: color, size: size); break;
      case "fadinggrid": myControl = SpinKitFadingGrid(color: color, size: size); break;
      case "ring": myControl = SpinKitRing(color: color, size: size); break;
      case "ripple": myControl = SpinKitRipple(color: color, size: size); break;
      case "spinningcircle": myControl = SpinKitSpinningCircle(color: color, size: size); break;
      case "spinninglines": myControl = SpinKitSpinningLines(color: color, size: size); break;
      case "squarecircle": myControl = SpinKitSquareCircle(color: color, size: size); break;
      case "dualring": myControl = SpinKitDualRing(color: color, size: size); break;
      case "pianowave": myControl = SpinKitPianoWave(color: color, size: size); break;
      case "dancingsquare": myControl = SpinKitDancingSquare(color: color, size: size); break;
      case "threeinout": myControl = SpinKitThreeInOut(color: color, size: size); break;
      case "wavespinner": myControl = SpinKitWaveSpinner(color: color, size: size); break;
      case "pulsinggrid": myControl = SpinKitPulsingGrid(color: color, size: size); break;
      case "rotatingcircle":
      default:
        myControl = SpinKitRotatingCircle(color: color, size: size);
    }

    return LayoutControl(control: control, child: myControl);
  }
}