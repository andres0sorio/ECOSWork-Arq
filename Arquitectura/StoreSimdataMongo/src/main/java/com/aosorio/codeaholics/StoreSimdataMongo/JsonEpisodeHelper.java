package com.aosorio.codeaholics.StoreSimdataMongo;


import com.google.gson.annotations.SerializedName;

/**
 * Created by snaphuman on 6/8/16.
 */
public class JsonEpisodeHelper {

	@SerializedName("_id")
	private String _id;
	private int cedula;
	private String fecha;
	private String hora;
	private int nivelDolor;
	private String medicamento;
	private String actividad;

	public String getActividad() {
		return actividad;
	}

	public void setActividad(String actividad) {
		this.actividad = actividad;
	}

	public String getMedicamento() {
		return medicamento;
	}

	public void setMedicamento(String medicamento) {
		this.medicamento = medicamento;
	}

	public String getId() { return _id; }

	public void setId(String _id) { this._id = _id; }

	public int getCedula() {
		return cedula;
	}

	public void setCedula(int cedula) {
		this.cedula = cedula;
	}

	public String getFecha() {
		return fecha;
	}

	public void setFecha(String fecha) {
		this.fecha = fecha;
	}

	public int getNivelDolor() {
		return nivelDolor;
	}

	public void setNivelDolor(int nivelDolor) {
		this.nivelDolor = nivelDolor;
	}

	public String getHora() { return hora; }

	public void setHora(String hora) {
		this.hora = hora;
	}

}
